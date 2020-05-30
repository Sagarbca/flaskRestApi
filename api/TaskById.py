from flask_restful import Resource
import  logging as logger
from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app import mongo,app
import json



class TaskById(Resource):

    def get(self,taskId):
        user = mongo.db.users.find_one({"_id" : ObjectId(taskId)})
        response = dumps(user)
        logger.debug("inside get method")
        return json.loads(response)

    def post(self,taskId):
        logger.debug("inside post method")
        json = request.json
        return {"message": "from post method Where task id = {}".format(taskId)}, 200

    def put(self,taskId):
        logger.debug("inside put method")
        _id = taskId
        json = request.get_json()
        name = json['name']
        email = json['email']
        password = json['password']
        # basic validation
        if name and email and password and request.method == 'PUT':
            # GENERATE HASH PASSWORD
            hashed_password = generate_password_hash(password)
            # Update the data
            users = mongo.db.users
            user_id = users.update_one({'_id' : ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set' : {'name': name, 'password': hashed_password, 'email': email}})
            update_user = users.find_one({'_id': user_id})
            output = {'name': update_user['name'], 'password': update_user['password'], 'email': update_user['email']}
            return jsonify({'result': output}, 201)
        else:
            return app.errorhandler


    def delete(self,taskId):
        mongo.db.users.delete_one({"_id" : ObjectId(taskId)})
        response = {"message" : "user deleted successfully"}
        return jsonify(response)
        logger.debug("inside delete method")
        return {"message": "from delete method"}, 200