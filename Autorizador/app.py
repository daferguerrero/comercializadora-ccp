from flask import Flask

from flask_restful import Api
from flask_jwt_extended import JWTManager
from vistas import VistaGenerarToken,VistaValidarToken
from datetime import timedelta


app = Flask(__name__)
app.debug = True
app.config['JWT_SECRET_KEY'] = 'cpp-key-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app_context = app.app_context()
app_context.push()



api=Api(app)
api.add_resource(VistaGenerarToken,'/token/generar')
api.add_resource(VistaValidarToken,'/token/validar')

jwt = JWTManager(app)