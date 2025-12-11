from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundo desde Python y Docker!"

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000 y accesible desde cualquier IP (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)
