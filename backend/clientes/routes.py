from flask import Blueprint,jsonify
from db import registrar_cliente,ver_clientes

client_bp=Blueprint("cliente",__name__)

@client_bp.route("/ver",methods=["GET"])
def client():
    resp=ver_clientes()
    return jsonify(resp)

@client_bp.route("/ver/<int:id>",methods=["GET"])
def buscar(id):
    resp={"cliente":f"especifico {id}"}
    return jsonify(resp)

@client_bp.route("/registrar",methods=["POST"])
def registrar():
    return jsonify({"message":"registro de clientes"})

@client_bp.route("/eliminar/<int:id>",methods=["DELETE"])
def eliminar(id):
    resp={"message":f"eliminar cliente {id}"}
    return jsonify(resp)      

@client_bp.route("/actualizar/<int:id>",methods=["PUT"])
def modificar(id):
    resp={"message":f"actualizar informacion de {id}"}
    return jsonify(resp)