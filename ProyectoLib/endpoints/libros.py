from flask import Blueprint, jsonify, request, Response
import pymongo

book_service = Blueprint(name="book_service", import_name=__name__)

@book_service.route('register', methods=['POST','GET'])
def Registro():
    if request.method == "POST":
        data = request.get_json()
        if "id_book" in data and "book_title" in data and "book_type" in data and "author" in data and "book_count" in data and "book_available" in data and "book_not_available" in data and "book_year" in data and "book_editorial" in data:
            if data["id_book"] != "" and data["book_title"] != "" and data["book_type"] != "" and data["author"] != "" and data["book_count"] != -1 and data["book_available"] != -1 and data["book_not_available"] != -1 and data["book_year"] != -1 and data["book_editorial"] != "" :
                libro_insertar = {
                    "id_book": data["id_book"],
                    "book_title": data["book_title"],
                    "book_type": data["book_type"],
                    "author": data["author"],
                    "book_count": data["book_count"],
                    "book_available": data["book_available"],
                    "book_not_available": data["book_not_available"],
                    "book_year": data["book_year"],
                    "book_editorial": data["book_editorial"]
                }
                try:
                    cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                    mongo_db = cliente_mongo["libreria"]
                    mongo_collections = mongo_db["libros"]
                    respuesta_mongo = mongo_collections.insert_one(libro_insertar)
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

@book_service.route('find', methods=['POST','GET'])
def find():
    if request.method == 'GET':
        data = request.get_json()
        if "id_book" in data and "book_title" in data and "book_type" in data:
            if data["id_book"] != "" and data["book_title"] != "" and data["book_type"] != "":
                try:
                    cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                    mongo_db = cliente_mongo["libreria"]
                    mongo_collections = mongo_db["libros"]
                    myquery = {
                        "id_book": data["id_book"],
                        "book_title": data["book_title"],
                        "book_type": data["book_type"]
                        }
                    respuesta_mongo = mongo_collections.find(myquery)
                    libros=[]
                    for libro in respuesta_mongo:
                        libros.append(
                        {
                        "id_book": libro.get("id_book"),
                        "book_title": libro.get("book_title"),
                        "book_type": libro.get("book_type"),
                        "author": libro.get("author"),
                        "book_count": libro.get("book_count"),
                        "book_available": libro.get("book_available"),
                        "book_not_available": libro.get("book_not_available"),
                        "book_year": libro.get("book_year"),
                        "book_editorial": libro.get("book_editorial")
                        })
                    return jsonify({
                        "data": libros
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
