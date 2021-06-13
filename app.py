import json

import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/minified', methods=['POST'])
def post_url():
    randomUUID = uuid.uuid1()
    return jsonify(status=200, url=randomUUID)

@app.route('/minified/<uuid>', methods=['GET'])
def resolve_url(uuid):
    return jsonify(status=200, url=f"http://www.example.com/{uuid}")

if __name__ == "__main__":
    app.run()
