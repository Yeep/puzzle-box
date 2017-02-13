from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('level2/level2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1338)