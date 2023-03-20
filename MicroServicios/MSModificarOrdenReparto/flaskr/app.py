from flaskr import create_app
from flask_restful import Api
from .modelos import db, OrdenReparto, OrdenRepartoSchema, modelos
from .vistas import VistaModificarOrdenReparto


app = create_app('default')
app_context= app.app_context()
app_context.push()

db.init_app(app)
db.drop_all()
db.create_all()
modelos.crear_default_orden_reparto()

api=Api(app)
api.add_resource(VistaModificarOrdenReparto,'/orden_reparto/modificar/<int:id_orden>')
