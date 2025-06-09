from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Service A (host: {socket.gethostname()}, IP Address: {socket.gethostbyname(socket.gethostname())})"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
