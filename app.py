from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API está funcionando!\nEssa é a versão 1.0"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/info')
def info():
    return jsonify({
        "app": "Minha API",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)