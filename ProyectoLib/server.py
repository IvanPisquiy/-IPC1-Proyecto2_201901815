##IMPORTS
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

## LLAMADAS ENPOINTS

from endpoints.libros import book_service
from endpoints.usuarios import user_service


app = Flask(__name__)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*")

##ENDPOINTS 
""" Blueprint
Registro de libros:

{
    "id_book": "",
    "book_title": "",
    "book_type": "",
    "author": "",
    "book_count": 0,
    "book_available": 0,
    "book_not_available": 0,
    "book_year": 0,
    "book_editorial": ""
}

Registro de Usuarios:
{
    "id_user": "",
    "user_display_name": "",
    "user_nickname": "",
    "user_password": "",
    "user_age": "",
    "user_career": "",
    "user_carnet": ""
}

"""

app.register_blueprint(book_service, url_prefix="/book")
app.register_blueprint(user_service, url_prefix="/user")


##ENDPOINTS
@app.route('/', methods = ['GET','POST','PUT'])
def init():
     return jsonify({
        "Curso"    : "Introducción a la programación y computación 1"
    })

## INIT
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='3000', debug = True)
