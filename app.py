from flask import Flask, jsonify
from informacion import informacion
import json

app = Flask(__name__)

#Testeo para ver si mi servidor responde con algo
@app.route('/ping')
def ping():
    return jsonify({"message": "Servidor funcionando perfectamente"})

#Ruta para obtener los productos
@app.route('/informacion', methods=['GET'])
def getInfo():
    with open('informacion.json', 'w') as json_file:
        json.dump(informacion, json_file)
    return jsonify({"informacion": informacion})

if __name__ == '__main__':
    app.run(debug=True, port=5000)