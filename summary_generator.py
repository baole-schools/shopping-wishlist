# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 08/11/2025
# Microservice B: Summary Generator

import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")
print("The microservice Summary Generator is running.")

while True:
    time.sleep(0.5)
    try:
        message = socket.recv_string()
        data = json.loads(message)
        print(f"Received message: {data}")

        prices = [float(product['price']) for product in data]
        total = sum(prices)
        max_price = max(prices)
        max_index = [idx for idx in range(len(data)) if prices[idx] == max_price]
        max_product = [data[idx]['name'] for idx in max_index]
        min_price = min(prices)
        min_index = [idx for idx in range(len(data)) if prices[idx] == min_price]
        min_product = [data[idx]['name'] for idx in min_index]

        response = {
            'count': len(prices),
            'total': total,
            'max_price': max_price,
            'max_product': max_product,
            'min_price': min_price,
            'min_product': min_product,
        }

        response = json.dumps(response)
        print(f"Responding: {response}")
        socket.send_string(response)

    except Exception as e:
        socket.send_string(json.dumps({'error': str(e)}))