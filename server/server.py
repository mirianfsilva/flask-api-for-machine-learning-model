import time, os, pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, make_response, Response
from flask_restplus import Api, fields, Resource
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


app = Flask(__name__)
CORS(app)

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Machine Learning Model API',
    description='Lorem Ipsum')

ns = api.namespace('ml_model', description='Lorem Ipsum')
model = pickle.load(open('./model.pkl','rb'))

parser = api.parser()


#TODO WIP

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5003, debug=True)