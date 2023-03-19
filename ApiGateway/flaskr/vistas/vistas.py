
from flask_restful import Resource
from flask import request
from .monitor import Monitor
import requests

class VistaAPIGenerarOrdenVenta(Resource):
    
    def post(self):
        monitor = Monitor()
        estado = monitor.ping()
          
        datosRecibir= {
            "tipoid":request.json["tipoid"],
            "identificacion":request.json["identificacion"],
            "nombre":request.json["nombre"],
            "direccion":request.json["direccion"],
            "telefono":request.json["telefono"],
            "estado_recibir":estado
        }
        
        response = requests.post('http://127.0.0.1:5000/orden/generar',json=datosRecibir,headers={"Content-Type": "application/json"},)

        print(response.text)
        return response.json()

class VistaAPISolicitarToken(Resource):

    def get(self):

        response = requests.post('http://127.0.0.1:5001/token/generar',headers={"Content-Type": "application/json", "apiKey": request.headers["apiKey"], "user": request.headers["user"]})

        print(response.text)
        return response.json()