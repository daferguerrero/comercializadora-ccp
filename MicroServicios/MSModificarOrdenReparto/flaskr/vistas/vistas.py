from flask_restful import Resource
from flask import request
from ..modelos import db, OrdenReparto, OrdenRepartoSchema


orden_reparto_schema = OrdenRepartoSchema()

class VistaModificarOrdenReparto(Resource):
    def get(self, id_orden):
        return orden_reparto_schema.dump(OrdenReparto.query.get_or_404(id_orden))

    def put(self, id_orden):
        ordenreparto = OrdenReparto.query.get_or_404(id_orden)
        ordenreparto.nombre_cliente = request.json.get('nombre_cliente')
        ordenreparto.direccion_entrega = request.json.get('direccion_entrega')
        ordenreparto.telefono = request.json.get('telefono')

        db.session.commit()
        return orden_reparto_schema.dump(OrdenReparto.query.get_or_404(id_orden))