import base64
import json

import jwt, os
from dotenv import load_dotenv
from flask import Flask, request, jsonify


app = Flask(__name__)

from models import *


@app.route("/")
def hello():
    return {
               "message": "hello world"
           }, 200

@app.route("/user",methods=["POST"])
def crearUsuario():
    data = request.json
    if not data:
        return {
                   "mensaje": "No hay datos"
               }, 400
    user = Usuario().create(**data)
    if user:
        return {
            "mensaje": "Usuario creado",
            "datos": user
        }
    else:
        return {
                   "message": "Error creando al usuario"
               }, 500

@app.route("/comida",methods=["POST"])
def crearComida():
    data = request.json
    if not data:
        return {
                   "mensaje": "No hay datos"
               }, 400
    user = Comida().create(**data)
    if user:
        return {
            "mensaje": "Comida creada",
            "datos": user
        }
    else:
        return {
                   "message": "Error creando la comida"
               }, 500

@app.route("/comida/<nickname>/<starttime>/<endtime>",methods=["GET"])
def obtenerComidas(nickname,starttime,endtime):
    try:
        if nickname is None or starttime is None or endtime is None:
            return {
                       "message": "Datos incompletos"
                   }, 400
        comidas = Comida().get_comida_by_time(nickname,starttime,endtime)
        print("Comidas "+str(comidas))
        if comidas:
            return {

                "datos": comidas
            }
        else:
            return {
                       "message": "No hay comidas de " + str(nickname)+" en la fecha indicada"
                   }, 400
    except Exception as e:
        print("ERROR "+str(e))
        return {
                   "message": "Error al obtener las comidas de "+str(nickname)
               }, 500

@app.route("/calorias/<nickname>/<starttime>/<endtime>",methods=["GET"])
def obtenerCalorias(nickname,starttime,endtime):
    try:
        if nickname is None or starttime is None or endtime is None:
            return {
                       "message": "Datos incompletos"
                   }, 400
        calorias = Comida().get_calories_by_time(nickname,starttime,endtime)

        if calorias:
            return calorias
        else:
            return {
                       "message": "Error al obtener las calorias de " + str(nickname)
                   }, 500
    except Exception as e:
        print("ERROR "+str(e))
        return {
                   "message": "Error al obtener las calorias de "+str(nickname)
               }, 500

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5002)
