import os
from app.main._init_ import main

from flask import (render_template,
                   redirect,
                   request, session)
from app.models.usuario import Usuario
from app._init_ import db

@main.route("/validarLogin", methods=["POST"])
def validarLogin():
    #idusuario = request.form.get("idusuario", default=0, type=int)
    usuario = request.form.get("usuario", default=0, type=str)
    clave = request.form.get("clave", default="", type=str)
    usuarioDB = Usuario.query.filter_by(usuario=usuario).first()
    if usuarioDB and usuarioDB.clave == clave:
        session['usuario'] = usuarioDB.usuario
        return redirect("/inicio")
    return redirect("/?bc=True")

@main.route("/", methods=["GET"])
def login():
    return render_template("login.html", badCredentials=request.args.get('bc', default=False, type=bool))

@main.route("/inicio", methods=["GET"])
def inicio():
    return render_template("inicio.html")

@main.route("/usuario", methods=["GET", "POST"])
def getUsuario():
    mesage = ''
    if request.method == 'POST':
        eliminar = request.form.get("eliminar")
        idusuario = request.form.get("idusuario")
        if not eliminar or eliminar == "":
            if not idusuario or idusuario == "":
                usuario = Usuario(request.form)
                db.session.add(usuario)
                mesage = "Registro exitoso"
            else:
                usuario = Usuario.query.filter_by(
                    idusuario=idusuario).first()
                usuario.nombre = request.form.get(
                    "nombre", default="", type=str)
                usuario.apellidos = request.form.get(
                    "clave", default="", type=str)
                usuario.idarea = request.form.get(
                    "estado", default="", type=int)
                mesage = "Actualizacion exitosa"
        else:
            usuario = Usuario.query.filter_by(idusuario=idusuario).first()
            db.session.delete(usuario)
            mesage = "Se eliminó correctamente"
        db.session.commit()
    return render_template("usuario.html",  msg=mesage)


@main.route("/usuario/<int:id>", methods=["GET"])
def searchUsuario(id):
    usuario = Usuario.query.filter_by(idusuario=id).first()
    if usuario is not None:
        resultado = usuario.to_full_json()
    else:
        resultado = {'status': 404}
    print(usuario)
    return resultado

@main.route("/operadores", methods=["GET", "POST"])
def getOperadores():
    mesage = ''
    if request.method == 'POST':
        eliminar = request.form.get("eliminar")
        idoperador = request.form.get("idoperador")
        if not eliminar or eliminar == "":
            if not idoperador or idoperador == "":
                operador = Operadores(request.form)
                db.session.add(operador)
                mesage = "Registro exitoso"
            else:
                operador = Operadores.query.filter_by(
                idoperador=idoperador).first()
                operador.dni = request.form.get(
                    "dni", default="", type=str)
                operador.nombre = request.form.get(
                    "nombre", default="", type=str)
                operador.apellido = request.form.get(
                    "apellido", default="", type=str)
                operador.fechanac = request.form.get(
                    "fechanac", default="", type=int)
                mesage = "Actualizacion exitosa"
        else:
            operador = Operadores.query.filter_by(idoperador=idoperador).first()
            db.session.delete(operador)
            mesage = "Se eliminó correctamente"
        db.session.commit()
    return render_template("operadores.html",  msg=mesage)

@main.route("/operadores/<int:id>", methods=["GET"])
def searchoperador(id):
    operador = operador.query.filter_by(idoperador=id).first()
    if operador is not None:
        resultado = operador.to_full_json()
    else:
        resultado = {'status': 404}
    print(operador)
    return resultado

@main.route("/materiales", methods=["GET", "POST"])
def getMateriales():
    mesage = ''
    if request.method == 'POST':
        eliminar = request.form.get("eliminar")
        idusuario = request.form.get("idusuario")
        if not eliminar or eliminar == "":
            if not idmateriales or idmateriales == "":
                materiales = Materiales(request.form)
                db.session.add(materiales)
                mesage = "Registro exitoso"
            else:
                usuarios = Usuario.query.filter_by(
                    idusuario=idusuario).first()
                usuarios.usuario = request.form.get(
                    "usuario", default="", type=str)
                usuarios.clave = request.form.get(
                    "clave", default="", type=str)
                usuarios.nombrecompleto = request.form.get(
                    "nombrecompleto", default="", type=str)
                mesage = "Actualizacion exitosa"
        else:
            materiales= Usuario.query.filter_by(idmateriales=idmateriales).first()
            db.session.delete(materiales)
            mesage = "Se eliminó correctamente"
        db.session.commit()
    return render_template("materiales.html",  msg=mesage)

@main.route("/materiales/<int:id>", methods=["GET"])
def searchMateriales(id):
    materiales = Materiales.query.filter_by(idmateriales=id).first()
    if materiales is not None:
        resultado = materiales.to_full_json()
    else:
        resultado = {'status': 404}
    return resultado
