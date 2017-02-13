from flask import Flask, render_template, request
from os import listdir
from os.path import isfile, join
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('level2/index.html')

@app.route('/gallery')
def gallery():
    path = join('static', 'pictures', request.args.get('path'))
    images = [f for f in listdir(path) if (isfile(join(path, f)))]
    return render_template('level2/gallery.html', path=path, images=images)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1338)