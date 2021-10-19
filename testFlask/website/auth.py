from flask import Blueprint, render_template,request
import datetime
from flask.helpers import url_for

from werkzeug.utils import redirect


auth = Blueprint('auth',__name__)

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido


@auth.route('/login')
def login():
    return render_template("Index.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sing-up')
def sing_up():
    return "<p>Sing Up</p>"

@auth.route('/MainPost', methods=['GET','POST'])
def enviosaux():
    if request.method == "POST":
        user = request.form["mn"]
        return redirect(url_for("/Main"))
        return  render_template("Main.html",data= user)
    else:
        return render_template("Main.html",data= "hi")


@auth.route('/Main', methods=['GET','POST'])
def envios():
    user = "hi"
    if request.method == "GET":
        print("ejecutado")
        pass
        #user = request.form["mn"]
        #user = request.args['mn']
      
    return  render_template("Main.html",data= user)

@auth.route('/test',methods=['GET','POST'])
def test():
    p1 = Persona("Estudainte Sergie", "Arizandieta")
    temas = ["Plantillas","Modelos","FSormularios","Vistas","Despligue"]
    fecha_actual = datetime.datetime.now()


    return render_template("test.html", 
    diccionario = {
        "nombre_persona":p1.nombre,
        "apellido_persona":p1.apellido,
        "Fecha_actual":fecha_actual, 
        "temas": temas } )