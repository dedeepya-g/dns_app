# US/us_server.py
from flask import Flask, request, jsonify
import socket
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci_request():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return "Bad Request", 400

    try:
        number = int(number)
    except ValueError:
        return "Bad Request", 400

    # DNS resolution
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Bad Request", 400

    # Query FS for Fibonacci number
    response = requests.get(f'http://fs:9090/fibonacci?number={number}')
    return (response.content, response.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

