from flask import Flask

from flask_restful import Api
from flask_jwt_extended import JWTManager
from vistas import VistaGenerarToken,VistaValidarToken
from datetime import timedelta
from modelos import db
from modelos import modelos


app = Flask(__name__)
app.debug = True
app.config['JWT_SECRET_KEY'] = 'cpp-key-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///CCP.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.drop_all()
db.create_all()
modelos.crear_default_configuracion()

api=Api(app)
api.add_resource(VistaGenerarToken,'/token/generar')
api.add_resource(VistaValidarToken,'/token/validar')

jwt = JWTManager(app)