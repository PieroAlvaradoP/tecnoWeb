from app._init_ import db
from sqlalchemy import Sequence

class Materiales(db.Model):
    __tablename__ = 'materiales'
    idmateriales= db.Column(db.Integer,primary_key=True)
    descripcion = db.Column(db.String(100), unique=False, nullable=False)
    precio = db.Column(db.Float(10), unique=False, nullable=False)
    cantidad= db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, form):

        if form.get('idmateriales') != "":
            self.idmateriales = form.get('idmateriales')

        self.descripcion = form.get('descripcion')
        self.precio = form.get('precio')
        self.cantidad = form.get('cantidad')

    def to_full_json(self):
        json_materiales = {
            'status': 200,
            'idmateriales': self.idmateriales,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad
        }
        return json_materiales

    @staticmethod
    def from_json(json_post):
        idmateriales = json_post.get('idmateriales')
        descripcion = json_post.get('descripcion')
        precio = json_post.get('precio')
        cantidad = json_post.get('cantidad')

        materiales = Materiales(
            idmateriales=idmateriales,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad
        )
        return materiales