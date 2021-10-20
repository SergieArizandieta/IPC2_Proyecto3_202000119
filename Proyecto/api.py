from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/events/' , methods=['POST'])
def post_event():
    data = open('data.txt','w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')

@app.route('/events/' , methods=['GET'])
def pet_event():
    data = open('data.txt','r+')


    return Response(response= data.read(),
    mimetype= 'text/plain',
    content_type='text/plain')   

if __name__ == '__main__':
    app.run(debug=True,port=5000)