# AS/as_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

records = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    records[hostname] = ip
    return "Registered", 201

@app.route('/query', methods=['GET'])
def query():
    hostname = request.args.get('hostname')
    if hostname in records:
        return jsonify({"hostname": hostname, "ip": records[hostname]}), 200
    return "Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53533)

