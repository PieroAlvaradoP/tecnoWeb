from app._init_ import db
from sqlalchemy import Sequence

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario= db.Column(db.Integer,primary_key=True)
    usuario = db.Column(db.String(50), unique=False, nullable=False)
    clave = db.Column(db.String(10), unique=False, nullable=False)
    nombrecompleto= db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, form):
        self.idusuario = form.get('idusuario')
        self.usuario = form.get('usuario')
        self.clave = form.get('clave')
        self.nombrecompleto = form.get('nombrecompleto')

    def to_full_json(self):
        json_usuario = {
            'status': 200,
            'idusuario': self.idusuario,
            'usuario': self.usuario,
            'clave': self.clave,
            'nombrecompleto': self.nombrecompleto
        }
        return json_usuario

    @staticmethod
    def from_json(json_post):
        idusuario = json_post.get('idusuario')
        usuario = json_post.get('usuario')
        clave = json_post.get('clave')
        nombrecompleto = json_post.get('nombrecompleto')

        usuarios = Usuario(
            idusuario=idusuario,
            nombre=usuario,
            clave=clave,
            estado=nombrecompleto
        )
        return usuarios