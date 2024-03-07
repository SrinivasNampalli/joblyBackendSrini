from flask import request, jsonify, Blueprint
from flask_restful import Api, Resource
from __init__ import app, db, cors
from datetime import datetime

ml_api = Blueprint('ml_api', __name__, url_prefix='/api/machinelearning')
api = Api(ml_api)

class MachineLearningAPI:
    class _Predict(Resource):
        def post(self):
            ''' Read data from json body '''
            body = request.get_json()
            print(body) 
            
            # Extract data from JSON body
            name = body.get('name', [''])[0]
            pclass = body.get('pclass', [0])[0]
            sex = body.get('sex', [''])[0]
            age = body.get('age', [0])[0]
            sibsp = body.get('sibsp', [0])[0]
            parch = body.get('parch', [0])[0]
            fare = body.get('fare', [0.0])[0]
            embarked = body.get('embarked', [''])[0]
            alone = body.get('alone', [True])[0]
            
            # Perform machine learning predictions
            prediction = perform_prediction(name, pclass, sex, age, sibsp, parch, fare, embarked, alone)
            print(prediction)
            
            return jsonify({'prediction': prediction})

    # Build REST API endpoint
    api.add_resource(_Predict, '/predict')

def perform_prediction(name, pclass, sex, age, sibsp, parch, fare, embarked, alone):
    # Placeholder for machine learning prediction logic
    # You would typically use your trained ML model here
    # For demonstration purposes, let's assume a simple rule-based prediction
    if sex == 'female':
        return 'Survived'
    else:
        return 'Not Survived'
