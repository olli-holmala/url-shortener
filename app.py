import json

from core.shortener import shorten, resolve
#import uuid
from flask import Flask, request, jsonify
import sqlite3
from persistence.db_init import init_db

app = Flask(__name__)


@app.route('/minified', methods=['POST'])
def post_url():
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    # Would need to check that this complies with our openapi expected structure.
    data = request.json
    long_url = data["url"]
    # This would still need a check of the DB to see if the URL already exists.
    cursor.execute(f""" REPLACE INTO full_urls (url) 
                        VALUES (?);""", (long_url,))
    uuid = cursor.lastrowid
    minifiedId = shorten(uuid)
    connection.commit()
    return jsonify(status=200, minified_url=f"http://localhost:5000/minified/{minifiedId}")

@app.route('/minified/<uuid>', methods=['GET'])
def resolve_url(uuid):
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    record_id = resolve(uuid)
    cursor.execute(f"SELECT url FROM full_urls WHERE id=(?);", (record_id,))
    records = cursor.fetchone()
    if(len(records) == 0):
      return(jsonify(status=500, reason=f"Internal Server error resolving {uuid}"))
    return jsonify(status=200, resolved_url=records[0])

if __name__ == "__main__":
    app.run()
