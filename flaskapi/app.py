from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Helm Testing API",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}, your API is working!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)