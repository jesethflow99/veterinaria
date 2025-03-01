from flask import Blueprint,jsonify,request
from db import *

client_bp=Blueprint("cliente",__name__)

@client_bp.route("/ver",methods=["GET"])
def client():
    resp=ver("clientes")
    return jsonify(resp)

@client_bp.route("/ver/<int:id>",methods=["GET"])
def buscar(id):
    resp=ver_1(id,"clientes",)
    return jsonify(resp)

@client_bp.route("/registrar",methods=["POST"])
def registrar():
    data=request.json
    return registrar_cliente(data)

@client_bp.route("/eliminar/<int:id>",methods=["DELETE"])
def eliminar_cliente(id):
    resp=eliminar(id,"clientes")
    return jsonify(resp)      

@client_bp.route("/actualizar/<int:id>",methods=["PUT"])
def modificar(id):
    resp={"message":f"actualizar informacion de {id}"}
    return jsonify(resp)