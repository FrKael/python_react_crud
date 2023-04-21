from flask import Flask, request
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

#mongousr
#mongopsw

app = Flask(__name__)
app.config['MONGO_URI']= "mongodb+srv://mongousr:mongopsw@pythonreactdb.c6tcn8h.mongodb.net/pythonreactdb?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    id = {
        'name': request.json["name"],
        'email': request.json['email'],
        'password': request.json['password']
    }
    result = db.insert_one(id)
    inserted_id = result.inserted_id
    return str(inserted_id)

if  __name__ == "__main__":
    app.run(debug = True)

@app.route('/users', methods=['GET'])
def getUser():
    return  'recived'

@app.route('/user/<id>', methods=['GET'])
def getUsers():
    return  'recived'

@app.route('/user/<id>', methods=['GET'])
def deleteUser():
    return  'recived'

@app.route('/user/<id>', methods=['PUT'])
def updateUser():
    return  'recived'


