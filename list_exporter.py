# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 08/11/2025
# Microservice D: List Exporter

import zmq
import time
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8888")
print("The microservice List Exporter is running.")

while True:
    time.sleep(0.5)
    try:
        message = socket.recv_string()
        data = json.loads(message)
        print(f"Received message: {data}")

        if not data:
            socket.send_string(json.dumps({'error': 'Invalid data'}))
            continue

        time_stamp = int(time.time())

        with open('list_export.json', 'w') as out_file:
            data = json.dumps(data)
            out_file.write(data)

        response = {
            'path': os.path.join(os.getcwd(), 'list_export.json'),
        }

        response = json.dumps(response)
        print(f"Responding: {response}")
        socket.send_string(response)

    except Exception as e:
        socket.send_string(json.dumps({'error': str(e)}))