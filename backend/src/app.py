from flask import Flask, request, jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

#mongousr
#mongopsw

app = Flask(__name__)
app.config['MONGO_URI']= "mongodb+srv://mongousr:mongopsw@pythonreactdb.c6tcn8h.mongodb.net/pythonreactdb?retryWrites=true&w=majority"
mongo = PyMongo(app)

#interaccion de  react y flask
CORS(app)


db = mongo.db.users

#creacion de usuarios usando metodo 'POST'
@app.route('/users', methods=['POST'])
def createUser():
    id = {
        'name': request.json["name"],
        'email': request.json['email'],
        'password': request.json['password']
    }
    result = db.insert_one(id)
    inserted_id = result.inserted_id
    #transforma a str y devuelve el id y el mensaje
    return jsonify({'_id': str(inserted_id),'message': 'Registro creado con éxito'})

#Lista todos los usuarios guardandolos en la lista 'users' dentro de la funcion
@app.route('/users', methods=['GET'])
def getUser():
    users=[]
    for doc in db.find():
        users.append({
            '_id':  str(ObjectId(doc['_id'])),
            'name':  doc['name'],
            'email':  doc['email'],
            'password':  doc['password']
        })
    return  jsonify(users)

#Obtener solo datos del usuario especifico segun se especifica por el '_id'
@app.route('/user/<id>', methods=['GET'])
def getUsers(id):
    user = db.find_one({'_id': ObjectId(id)})
    print(user)
    return  jsonify({
        '_id': str(user['_id']),
        'name':  user['name'],
        'email':  user['email'],
        'password':  user['password']
    })

#elimina usuarios (en postman no debe haber nada en el request body)
@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return  'recivied'

#actualiza usuarios
@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    }})
    return  jsonify({'msg': 'user updated'})

if  __name__ == "__main__":
    app.run(debug = True)