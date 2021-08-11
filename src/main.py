"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify
from models import db, Task
#from models import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://flask4p1:123321...@85.10.205.173:3306/flaskapi" #Conexión con la DB (base de datos)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# generate sitemap with all your endpoints
@app.route('/') #Decorador 
def home():
    return jsonify({"mensaje": "Bienvenidos a mi APP :D"})

@app.route('/tareas', methods=['PUT' ]) #Decorador 
def actualizar_tareas():
    return jsonify({"mensaje_via_put": "Mensaje via PUT"})


@app.route('/tareas<id>', methods=['GET' ]) #Decorador 
def obtener_detalle_tareas(id):
    return jsonify({"mensaje_via_get": "Mensaje via GET"})

@app.route('/tareas', methods=['GET']) #Decorador 
def obtener_tareas():
    tasks = Task.query.all()
    return jsonify({"mensaje_via_get": "Mensaje via GET"})

        
@app.route('/tareas', methods=['POST']) #Decorador 
def obtener_tareas1():
    return jsonify({"mensaje_via_get": "Mensaje via Post"})

#@app.route('/tareas', methods=['PUT']) #Decorador 
#def obtener_tareas2():
#    return jsonify({"mensaje_via_get": "Mensaje via Put"})

@app.route('/tareas', methods=['DELETE']) #Decorador 
def obtener_tareas3():
    return jsonify({"mensaje_via_get": "Mensaje via Delete"})


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
