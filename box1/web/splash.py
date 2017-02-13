from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('splash.html', hostname=socket.gethostname(), port=1337)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)