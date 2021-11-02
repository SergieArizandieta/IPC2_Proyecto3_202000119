from flask import Flask, Response, request
from flask_cors import CORS
from LecturaData import LecturaData


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})


@app.route('/events/', methods=['POST'])
def post_events():
    dataRquestesd = request.data.decode('utf-8')
    #dataRquestesd = actualizar(dataRquestesd)

    data = open('data.xml', 'w+')
    data.write(dataRquestesd)
    data.close()
    
    #print(request.data.decode('utf-8') + " data recibida")
    LecturaData()

    return Response(response='Confirmado')
    
    ''' return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')'''


@app.route('/events/', methods=['GET'])
def get_events():
    
    data = open('data.xml', 'r',encoding="utf-8").read()
  
    return Response(response=data,
                    mimetype='text/plain',
                    content_type='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
