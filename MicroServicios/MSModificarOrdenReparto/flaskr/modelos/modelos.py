from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# import enum

db = SQLAlchemy()


class OrdenReparto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(128))
    direccion_entrega = db.Column(db.String(128))
    telefono = db.Column(db.String(10))

    def __repr__(self):
        return "{}-{}-{}".format(self.nombre_cliente, self.direccion_entrega, self.telefono)

class OrdenRepartoSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = OrdenReparto
         include_relationships = True
         load_instance = True

def crear_default_orden_reparto():
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Pepito", direccion_entrega="Calle 45 # 23-64", telefono='3101234567')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Juan", direccion_entrega="Avenida 64 # 10-23", telefono='3215874521')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="María", direccion_entrega="Transv. 23 # 14-98", telefono='31123658745')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Carlos", direccion_entrega="Calle 125 # 14-54", telefono='3203659874')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Josefa", direccion_entrega="Carrera 14 # 14-68", telefono='3108965412')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Ana", direccion_entrega="Carrera 12 # 45-65", telefono='35023654125')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Gustavo", direccion_entrega="Calle 65b # 56-87", telefono='31236952147')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Pedro", direccion_entrega="Carrera 7 # 11A-23", telefono='3153695821')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="David", direccion_entrega="Avenida américas # 125-65", telefono='310876145')
    db.session.add(nueva_orden_reparto)
    nueva_orden_reparto= OrdenReparto(nombre_cliente="Hugo", direccion_entrega="Calle 45 # 23-64", telefono='3101234567')
    db.session.add(nueva_orden_reparto)
    db.session.commit()
