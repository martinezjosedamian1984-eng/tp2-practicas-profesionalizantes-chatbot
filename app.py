
#Nuestros aervidores
#Importamos las librerias necesarias
from flask import Flask, render_template, request, jsonify
from reglas import sistema_experto 

app = Flask(__name__)

#crear las rutas
#ruta raiz - /
#Metodos o verbos HTTP - GET, POST, PUT, DELETE, PATCH
@app.route('/')
def inicio():
    return render_template('index.html')

#crear la ruta que responde a las peticiones del usuario
@app.route("/consulta", methods=["POST"])
def consulta():
    mensaje = request.json["mensaje"]
    respuesta = sistema_experto(mensaje)
    return jsonify({"respuesta": respuesta})

#activando el servidor
if __name__ == '__main__':
    app.run(debug=True)