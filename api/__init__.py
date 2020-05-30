from flask_restful import Api
from app import app
from .Task import Task
from .TaskById import TaskById
from flask import jsonify,request

restServer = Api(app)

restServer.add_resource(Task,"/api/v1/task")
restServer.add_resource(TaskById,"/api/v1/task/<string:taskId>")

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : "error in routing or some fields"
    }
    response = jsonify(message)
    response.status_code = 404
    return response