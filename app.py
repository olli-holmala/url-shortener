import json

from shortener import shorten, resolve
#import uuid
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/minified', methods=['POST'])
def post_url():
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    data = request.json
    long_url = data["url"]
    cursor.execute(f""" INSERT INTO full_urls (url) 
                        VALUES (?);""", (long_url,))
    uuid = cursor.lastrowid
    print(f"UUID: {uuid}")
    minifiedId = shorten(uuid)
    connection.commit()
    return jsonify(status=200, url=f"http://localhost:5000/minified/{minifiedId}")

@app.route('/minified/<uuid>', methods=['GET'])
def resolve_url(uuid):
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    record_id = resolve(uuid)
    cursor.execute(f"SELECT url FROM full_urls WHERE id=(?);", (record_id,))
    record = cursor.fetchone()
    return jsonify(status=200, url=record)

if __name__ == "__main__":
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    app.run()
