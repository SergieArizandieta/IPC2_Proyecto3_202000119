from flask import Flask, Response, request,jsonify
from flask_cors import CORS
from LecturaData import LecturaData,GenrarSalida,GenrarSalidaPDF
import json
import pdfkit
import webbrowser
from Operaciones import ResumenIVAfechaNIT,genrarPDFechaNit,GenerarGrafo,genrarGRAFPRango,ResumenPorRango,genrarPDFRango
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origin": "*"}})
#CORS (app)

@app.route ("/resume_rango_Iva_FechaGrafoPDF/", methods=['POST'])
def resume_rango_Iva_FechaGrafoPDF():
    
    #pdfkit.from_url('./ResumenRango.HTML', 'ResumenRango.pdf')
    

    pdfkit.from_file('ResumenRango.html', 'out.pdf')
    path = 'ResumenRango.pdf'
    webbrowser.open_new(path)

    response =  "Se genero PDF del grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_Iva_FechaGrafo/", methods=['POST'])
def resume_rango_Iva_FechaGrafo():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    op = request.json['Opcion'] 
    genrarGRAFPRango(fechaS,fechaF,op)
    response =  "Se genero Grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_Iva_FechaPDF/", methods=['POST'])
def resume_rango_Iva_FechaPDF():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    op = request.json['Opcion'] 
    genrarPDFRango(fechaS,fechaF,op)
    response =  "Se genero PDF"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_Iva_Fecha/", methods=['POST'])
def resume_rango_Iva_Fecha():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    op = request.json['Opcion'] 
    
    response =  ResumenPorRango(fechaS,fechaF,op)

    print(response)
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_Iva_FechaGrafo/", methods=['POST'])
def resume_Iva_FechaGrafo():
    fecha = request.json['date']
    nit = request.json['nit']
    GenerarGrafo(fecha,nit)
    response =  "Se genero PDF"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_Iva_FechaPDF/", methods=['POST'])
def resume_Iva_FechaPDF():
    fecha = request.json['date']
    nit = request.json['nit']
    genrarPDFechaNit(fecha,nit)
    response =  "Se genero Grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_Iva_Fecha/", methods=['POST'])
def resume_Iva_Fecha():
    fecha = request.json['date']
    nit = request.json['nit']
    response =  ResumenIVAfechaNIT(fecha,nit)
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route('/events/', methods=['POST'])
def post_events():
    dataRquestesd = request.data.decode('utf-8')
    
    data = open('data.xml', 'w+')
    data.write(dataRquestesd)
    data.close()
    
    LecturaData()

    return Response(response='Confirmado xml entrada')
    

@app.route('/eventsPDF/', methods=['GET'])
def get_eventsPDF():
    
    data = GenrarSalida()
    GenrarSalidaPDF(data)
    return Response(response='Se genero PDF')   

@app.route('/events/', methods=['GET'])
def get_events():
    
    data = GenrarSalida()
    return Response(response=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
