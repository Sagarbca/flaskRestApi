from flask_restful import Resource
import  logging as logger
from flask import request


class TaskById(Resource):

    def get(self,taskId):
        logger.debug("inside get method")

        return {"message": "from get method Where task id = {}".format(taskId)}, 200

    def post(self,taskId):
        logger.debug("inside post method")
        json = request.json
        return {"message": "from post method Where task id = {}".format(taskId)}, 200

    def put(self,taskId):
        logger.debug("inside put method")
        return {"message": "from put method"}, 200

    def delete(self,taskId):
        logger.debug("inside delete method")
        return {"message": "from delete method"}, 200