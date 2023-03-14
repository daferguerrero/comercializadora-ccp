from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db = SQLAlchemy()



class Configuracion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    apiKey = db.Column(db.String())
   

class ConfiguracionSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Configuracion
         include_relationships = True
         load_instance = True


def crear_default_configuracion():
        nueva_configuracion= Configuracion(user="cpp_reparto", apiKey="IPE56EOqtwRFeo7TCh6AQyimpqcPY0DIRxZFoni4OIPQ5DklmpCh4R3ocf1GP4hz")
        db.session.add(nueva_configuracion)
        db.session.commit()