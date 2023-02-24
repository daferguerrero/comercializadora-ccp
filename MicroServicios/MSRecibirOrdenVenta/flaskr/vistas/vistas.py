
from flask_restful import Resource
from flask import request
import json
from ..modelos import db,Orden, OrdenSchema


orden_schema = OrdenSchema()

class VistaRecibirOrdenVenta(Resource):

    def post(self):
        code_error='0'
        descripcion='OK'
        numero_orden=''
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

        return {'cod_error':code_error,'descripcion':descripcion,'numero_orden':numero_orden}







