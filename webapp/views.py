import os
import redis

from flask import Flask, request

app = Flask(__name__)

app.config.from_object('config')

redis_instance = redis.StrictRedis(
    host = app.config['REDIS_HOST'],
    port = app.config['REDIS_PORT'],
    password = app.config['REDIS_PASSWORD'],
    decode_responses=True
)

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':

        payload = request.get_json()

        redis_instance.set(payload["key"], payload["value"])

        return '', 204

@app.route('/read/<key>', methods=['GET'])
def read(key):
    if request.method == 'GET':
        return redis_instance.get(key)
