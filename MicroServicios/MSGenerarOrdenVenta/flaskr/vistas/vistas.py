
from flask_restful import Resource
from flask import request
import json
from ..modelos import db,Orden, OrdenSchema
import requests


orden_schema = OrdenSchema()

class VistaGenerarOrdenVenta(Resource):
    
    def post(self):
        code_error='0'
        descripcion='OK'
        numero_orden=''
        flag=request.json["estado_recibir"]
        if flag=='true':    
          
          datosRecibir= {
            "tipoid":request.json["tipoid"],
            "identificacion":request.json["identificacion"],
            "nombre":request.json["nombre"],
            "direccion":request.json["direccion"],
            "telefono":request.json["telefono"],
            "estado_recibir":request.json["estado_recibir"]
            
           }
          
          response = requests.post('http://127.0.0.1:5001/orden/recibir',json=datosRecibir,headers={"Content-Type": "application/json"},)

          print(response.text)
          return response.json()
          
        
        elif flag=='false':
            nueva_orden = Orden(
                tipoid = request.json["tipoid"],
                identificacion = request.json["identificacion"],
                nombre =request.json["nombre"],
                direccion = request.json["direccion"],
                telefono = request.json["telefono"],
            )
            db.session.add(nueva_orden)
            db.session.commit()
            orden_schema.dump(nueva_orden)
            numero_orden=nueva_orden.id
        else: 
               code_error='2'
               descripcion='Flag estado_recibir no esta definido'

        return {'cod_error':code_error,'descripcion':descripcion,'numero_orden':numero_orden}
            
        
        
  


  
