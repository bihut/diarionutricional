"""Application Models"""
import json
import sys

import bson, os
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import time

load_dotenv()

DATABASE_URL='mongodb://angel:123456@localhost:27017/?authMechanism=DEFAULT'
client = MongoClient(DATABASE_URL)
db = client.diarionutricional

class Usuario:
    def __init__(selfs):
        return

    def create(self,nombre,peso,altura,nickname):
        user = db.usuarios.insert_one({
            "nombre":nombre,
            "peso":peso,
            "altura":altura,
            "nickname":nickname
        })

        return self.get_by_id(user.inserted_id)
    def get_by_id(self, userid):
        user = db.usuarios.find_one({"_id": bson.ObjectId(userid)})
        if not user:
            return
        user["_id"] = str(user["_id"])
        return user

class Comida:
    def __init__(selfs):
        return

    def create(self, platos,user):
        #for plato in platos:
        #    Plato.create(plato['descripcion'],plato['calorias'])
        comida = db.comidas.insert_one({
            "platos": platos,
            "user":user,
            "timestamp":time.time()
        })
        return self.get_by_id(comida.inserted_id)

    def get_by_id(self, comidaid):
        comida = db.comidas.find_one({"_id": bson.ObjectId(comidaid)})
        if not comida:
            return
        comida["_id"] = str(comida["_id"])
        return comida

    def get_comida_by_time(self, userid,starttime,endtime):
        """Get all books by category for a particular user"""
        try:
            comidas= db.comidas.find({"user": str(userid),"timestamp":
                {'$gte': int(starttime),
                                       '$lte': int(endtime)}
                })
            return [{**comida, "_id": str(comida["_id"])} for comida in comidas]
        except Exception as e:
            print("ERROR "+str(e))

    def get_calories_by_time(self, userid, starttime, endtime):
        """Get all books by category for a particular user"""
        try:
            comidas = self.get_comida_by_time(userid,starttime,endtime)
            caloriastotales=0
            print("comidas:"+str(comidas))
            for pl in comidas[0]['platos']:
                print("PLA:" + str(pl))
                caloriastotales += pl['calorias']

            return {"caloriastotales":caloriastotales,"user":userid,"starttime":starttime,"endtime":endtime}
        except Exception as e:
            print("ERROR " + str(e))