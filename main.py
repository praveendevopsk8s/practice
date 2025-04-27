from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Smart Flask App!"})

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({"result": a + b})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify({"result": a * b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

