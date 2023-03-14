from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
import requests

class VistaGenerarToken(Resource):
    
    def post(self):
     usuario=request.json["usuario"]
     apikey=request.json["apikey"]
     token_de_acceso = create_access_token(identity=usuario)
     return {"mensaje": "Generación de token exitosa", "token": token_de_acceso}
    
class VistaValidarToken(Resource):
    @jwt_required()
    def post(self):
     return {"msg":"OK"}
