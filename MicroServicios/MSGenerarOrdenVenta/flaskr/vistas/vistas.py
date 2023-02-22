
from flask_restful import Resource
import json


class VistaGenerarOrdenVenta(Resource):
    
    def post(self):

        respuesta ={
            "cod_error":"0",
            "descripcion":"OK"
        }

        return json.dumps(respuesta)
