import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello AWS! This is my Hello World CICD running on host %s\n' % socket.gethostname()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)