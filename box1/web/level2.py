from flask import Flask, render_template, request, session
from base64 import b64encode
from subprocess import call
from os import listdir
from os.path import isfile, join
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'AnotherSecretKey'
api = Api(app)

@app.route('/')
def index():
    return render_template('level2/index.html')

@app.route('/gallery')
def gallery():
    return render_template('level2/gallery.html')

@app.route('/winner', methods=['POST'])
def winner():
    user_password = request.form['password']

    with open('secrets/password') as password_file:
        password = password_file.read()

    if password == user_password:
        session['secret'] = True
        return render_template('level2/winner.html')
    else:
        session['secret'] = False
        return render_template('level2/nope.html')

def createFileResponse(path, file):
    with open(join(path, file), "rb") as f:
        data = b64encode(f.read())
    return {'name': file, 'data': data}

class DirectoryListing(Resource):
    def get(self, path = '.'):
        os_path = join('static', path)
        images = [f for f in listdir(os_path) if (isfile(join(os_path, f)))]
        return list(map(lambda image: createFileResponse(os_path, image), images))

class Lock(Resource):
    def post(self):
        if session['secret']:
            call(["sudo", "../close_box"])

class Unlock(Resource):
    def post(self):
        if session['secret']:
            call(["sudo", "../open_box"])


api.add_resource(DirectoryListing, '/api/directory/<string:path>', '/api/directory')

api.add_resource(Lock, '/api/box/lock')

api.add_resource(Unlock, '/api/box/unlock')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=1338)