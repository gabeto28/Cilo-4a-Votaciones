from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorPartidos import ControladorPartidos

miCrontroladorCandidatos = ControladorCandidatos()
miCrontroladorMesas = ControladorMesas()
miCrontroladorPartidos = ControladorPartidos()
###################################################################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


###################################################################################

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miCrontroladorCandidatos.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])

def crearCandidatos():
    data = request.get_json()
    json = miCrontroladorCandidatos.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json = miCrontroladorCandidatos.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidatos(id):
    json = miCrontroladorCandidatos.delete(id)
    return jsonify(json)

###################################################################################
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miCrontroladorMesas.index()
    return jsonify(json)


@app.route("/mesas", methods=['POST'])
def crearMesas():
    data = request.get_json()
    json = miCrontroladorMesas.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json = miCrontroladorMesas.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesas(id):
    json = miCrontroladorMesas.delete(id)
    return jsonify(json)


###################################################################################

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
