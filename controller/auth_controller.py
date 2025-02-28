# controller/auth_controller.py
import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from controller.db_connection import db

usuarios = db.usuarios  # Colección de usuarios

# Función para verificar la contraseña
def verificar_contraseña(password, password_hash):
    return bcrypt.checkpw(password.encode('utf-8'), password_hash)

# Función de login
def login():
    datos = request.json
    matricula = datos.get("matricula")
    password = datos.get("password")

    if not matricula or not password:
        return jsonify({"error": "Matrícula y contraseña son requeridos"}), 400

    usuario = usuarios.find_one({"matricula": matricula})

    if usuario and verificar_contraseña(password, usuario["password"].encode('utf-8')):
        token = create_access_token(identity={"matricula": matricula})
        return jsonify({"mensaje": "Login exitoso", "token": token}), 200
    else:
        return jsonify({"error": "Matrícula o contraseña incorrectos"}), 401
