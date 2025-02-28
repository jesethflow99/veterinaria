from flask import Flask, jsonify,redirect,url_for
from clientes.routes import client_bp

app = Flask(__name__)
app.register_blueprint(client_bp,url_prefix="/cliente")

@app.route("/")
def index():
    return jsonify({"message":"hola mundo"})
    

if __name__ == "__main__":
    app.run(debug=True)
