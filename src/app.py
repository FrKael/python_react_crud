from flask import Flask, request
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']="mongodb+srv://mongouser:mongopassword@pythonreactdb.fi46pmk.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert_one({
        'name': request.json["name"],
        'email': request.json['email'],
        'password': request.json['password']
    })
    result = db.insert_one(id)
    inserted_id = result.inserted_id
    return 'recieved'

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

if  __name__ == "__main__":
    app.run(debug = True)
