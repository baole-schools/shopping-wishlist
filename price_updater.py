# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 08/11/2025
# Microservice C: Price Updater

import zmq
import time
import json

price_history = []

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7777")
print("The microservice Price Updater is running.")

while True:
    time.sleep(0.5)
    try:
        message = socket.recv_string()
        data = json.loads(message)
        print(f"Received message: {data}")

        if not data:
            socket.send_string(json.dumps({'error': 'Invalid data'}))
            continue
        name, price, updated = data["name"], data["price"], data["updated"]
        try:
            float(updated)
            if float(updated) < 0:
                socket.send_string(json.dumps({'error': 'Invalid data'}))
        except Exception as e:
            socket.send_string(json.dumps({'error': str(e)}))

        updated = str(round(float(updated), 2))

        found = False
        response = dict()

        for product in price_history:
            if product['name'] == name:
                if float(product['price'][-1]) == float(price):
                    product['price'].append(updated)
                    response = product
                    found = True
                    break

        if not found:
            product = dict()
            product['name'] = name
            product['price'] = [price, updated]
            price_history.append(product)
            response = product

        response = json.dumps(response)
        print(f"Responding: {response}")
        socket.send_string(response)

    except Exception as e:
        socket.send_string(json.dumps({'error': str(e)}))