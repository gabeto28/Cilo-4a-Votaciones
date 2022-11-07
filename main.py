from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

###################################################################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


###################################################################################
#################################CANDIDATOS########################################
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miCrontroladorCandidatos.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json = miCrontroladorCandidatos.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidatos(id):
    json = miCrontroladorCandidatos.show(id)
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
#################################PARTIDOS########################################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miCrontroladorPartidos.index()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miCrontroladorPartidos.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartidos(id):
    json = miCrontroladorPartidos.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json = miCrontroladorPartidos.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartidos(id):
    json = miCrontroladorPartidos.delete(id)
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
