from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from  modelos import Configuracion

class VistaGenerarToken(Resource):
    
    def post(self):

        apikey = None
        user =None
        if "user" in request.headers:
            user = request.headers["user"]
        if not user:
            return {
                "msg": "User key es obligatoria!",
                "token": None,
                "error": "Unauthorized"
            }, 401
        configuracion =  Configuracion.query.filter(Configuracion.user==user).first()
        if  not configuracion:
            return {
                "msg": "User key es es inválida",
                "token": None,
                "error": "Unauthorized"
            }, 401
        if "apiKey" in request.headers:
            apikey = request.headers["apiKey"]
        if not apikey or not configuracion or apikey!=configuracion.apiKey:
            return {
                "msg": "apiKey es obligatoria o es inválida",
                "token": None,
                "error": "Unauthorized"
            }, 401
        
        token_de_acceso = create_access_token(identity=user)
        return {"msg": "Generación de token exitosa", "token": token_de_acceso}
        
class VistaValidarToken(Resource):
    @jwt_required()
    def post(self):
     return {"msg":"OK"}
