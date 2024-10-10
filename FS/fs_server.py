# FS/fs_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']
    # TODO: Send UDP registration to AS
    return "Registered", 201

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    try:
        number = int(number)
        fib = fibonacci_number(number)
        return jsonify(fibonacci=fib), 200
    except ValueError:
        return "Bad Request", 400

def fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)

