from flask import Flask, render_template, request
from os import listdir
from os.path import isfile, join
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('level2/index.html')

@app.route('/gallery')
def gallery():
    return render_template('level2/gallery.html')

def createFileResponse(path, file):
    with open(join(path, file), "rb") as f:
        data = f.read().encode("base64")
    return {'name': file, 'data': data}

class DirectoryListing(Resource):
    def get(self, path = '.'):
        os_path = join('static', 'pictures', path)
        images = [f for f in listdir(os_path) if (isfile(join(os_path, f)))]
        return list(map(lambda image: createFileResponse(os_path, image), images))

api.add_resource(DirectoryListing, '/api/directory/<string:path>', '/api/directory')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1338)