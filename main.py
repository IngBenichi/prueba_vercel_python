from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "¡Hola desde Flask en Vercel!"})


# Este bloque es necesario para que Vercel detecte el handler
def handler(environ, start_response):
    return app(environ, start_response)