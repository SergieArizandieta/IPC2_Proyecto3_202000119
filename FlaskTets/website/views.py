from flask import Blueprint
from flask import Flask, Response, request
from website.auth import temas
views = Blueprint('views',__name__)

from flask_cors import CORS
cors = CORS(views, resources={r"/*": {"origin": "*"}})

@views.route('/')
def home():
    return "<h1>Test</h1>"

@views.route('/events/', methods=['POST'])
def post_events():
    dataRquestesd = request.data.decode('utf-8')
    #dataRquestesd = actualizar(dataRquestesd)

    data = open('data.xml', 'w+')
    data.write(dataRquestesd)
    data.close()
    
    #print(request.data.decode('utf-8') + " data recibida")

    print(dataRquestesd , " post")
    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')


@views.route('/events/', methods=['GET'])
def get_events():
    data = open('data.xml', 'r+')
    dataleida = data.read()
    print(dataleida , " get")
    temas.append(dataleida)
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')
