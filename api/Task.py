from flask_restful import Resource
import  logging as logger
from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app import mongo,app
import json

class Task(Resource):

    def get(self):
        logger.debug("inside get method")
        users = mongo.db.users.find()
        response = dumps(users)
        return json.loads(response)

    def post(self):
        logger.debug("inside post method")
        json = request.get_json()
        name =  json['name']
        email = json['email']
        password = json['password']
        #basic validation
        if name and email and password and request.method == 'POST':
            #GENERATE HASH PASSWORD
            hashed_password = generate_password_hash(password)
            #Insert the data
            users = mongo.db.users
            user_id = users.insert({'name': name, 'password': hashed_password,'email' : email})
            new_user = users.find_one({'_id': user_id})
            output = {'name': new_user['name'], 'password': new_user['password'], 'email': new_user['email']}
            return jsonify({'result': output},201)
        else:
            return not_found()

    def put(self):
        logger.debug("inside put method")
        return {"message": "from put method"}, 200

    def delete(self):
        logger.debug("inside delete method")
        return {"message": "from delete method"}, 200


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : "error in routing or some fields"
    }
    response = jsonify(message)
    response.status_code = 404
    return response