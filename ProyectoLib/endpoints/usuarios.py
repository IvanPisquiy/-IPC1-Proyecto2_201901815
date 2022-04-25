from flask import Blueprint, jsonify, request, Response
import pymongo

user_service = Blueprint(name="user_service", import_name=__name__)

@user_service.route('register', methods=['POST','GET'])
def Registro():
    if request.method == "POST":
        data = request.get_json()
        if "id_user" in data and "user_display_name" in data and "user_nickname" in data and "user_password" in data and "user_age" in data and "user_career" in data and "user_carnet" in data :
            if data["id_user"] != "" and data["user_display_name"] != "" and data["user_nickname"] != "" and data["user_password"] != "" and data["user_age"] != 0 and data["user_career"] != "" and data["user_carnet"] != -1 :
                user_insertar = {
                    "id_user": data["id_user"],
                    "user_display_name": data["user_display_name"],
                    "user_nickname": data["user_nickname"],
                    "user_password": data["user_password"],
                    "user_age": data["user_age"],
                    "user_career": data["user_career"],
                    "user_carnet": data["user_carnet"]
                }
                try:
                    cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                    mongo_db = cliente_mongo["libreria"]
                    mongo_collections = mongo_db["usuarios"]
                    respuesta_mongo = mongo_collections.insert_one(user_insertar)
                    return jsonify({
                        "status": "200",
                        "mensaje": "response"
                    }),200
                except Exception as e:
                    return jsonify({
                        "estado": "-3",
                        "mensaje": e
                    }),201
            else:
                return jsonify({
                    "estado": "400",
                    "mensaje": "Bad request"
                }),400
        else:
            return jsonify({
                "estado": "400",
                "mensaje": "Bad request"
            }),400
    else:
        return jsonify({
            "estado": "501",
            "mensaje": "Not implemented"
        }),501

@user_service.route('login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if "user_nickname" in data and "user_nickname" in data :
            if data["user_nickname"] != "" and data["user_nickname"] != "":
                try:
                    cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                    mongo_db = cliente_mongo["libreria"]
                    mongo_collections = mongo_db["usuarios"]
                    myquery = {
                        "user_nickname": data["user_nickname"],
                        "user_password": data["user_password"],
                        }
                    respuesta_mongo = mongo_collections.find(myquery)
                    usuarios=[]
                    for usuario in respuesta_mongo:
                        usuarios.append(
                        {
                        "id_user": usuario.get("id_user"),
                        "user_display_name": usuario.get("user_display_name"),
                        "user_nickname": usuario.get("user_nickname"),
                        "user_password": usuario.get("user_password"),
                        "user_age": usuario.get("user_age"),
                        "user_career": usuario.get("user_career"),
                        "user_carnet": usuario.get("user_carnet")
                        })
                    return jsonify({
                        "data": usuarios
                    }),200
                except Exception as e:
                    return jsonify({
                    "estado": "-3",
                    "mensaje": e
                    }),201
            else:
                return jsonify({
                    "estado": "400",
                    "mensaje": "Bad request"
                }),400
        else:
            return jsonify({
                "estado": "400",
                "mensaje": "Bad request"
            }),400
    else:
        return jsonify({
            "estado": "501",
            "mensaje": "Not implemented"
        }),501