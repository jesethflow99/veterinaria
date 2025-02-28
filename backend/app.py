from flask import Flask, jsonify,redirect,url_for
from db import registrar_cliente, ver_clientes

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(ver_clientes())

@app.route("/registrar")
def registrar():
    resp=registrar_cliente({
        "id": 5567,
        "nombre": "Gael gonzales torres",
        "contacto": "6352330967",
        "domicilio": "Av.tierra santa 220, 31522"
    })
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)
