from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db = SQLAlchemy()



class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipoid = db.Column(db.String(5))
    identificacion = db.Column(db.Integer)
    nombre = db.Column(db.String(128))
    direccion = db.Column(db.String(128))
    telefono = db.Column(db.String(10))


    def __repr__(self):
        return "{}-{}-{}-{}".format(self.tipoid, self.identificacion, self.nombre, self.direccion,self.telefono)

class OrdenSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Orden
         include_relationships = True
         load_instance = True
