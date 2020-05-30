from flask import Flask
#This comes from  the python module
import logging as logger
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
#to run in the debug mode
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

app.config['MONGODB_NAME'] = 'learn-python'
app.config['MONGO_URI'] = 'mongodb+srv://sagar-verma:1Pinkiverma@nodejs-api-i4atr.mongodb.net/learn-python?retryWrites=true&w=majority'

mongo = PyMongo(app)

if __name__ == "__main__" :
    from api import *
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
