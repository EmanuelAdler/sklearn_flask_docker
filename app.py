# Local imports
import datetime

# Third part imports
from flask import request
import pandas as pd

from ms import app
from ms.functions import get_model_response, get_predict_all


model_name = "Random Forest model for water potability prediction"
model_file = 'random_forest.joblib'
version = "v1.0.0"


@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}

    result["name"] = model_name
    result["version"] = version

    return result


@app.route('/health', methods=['GET'])
def health():
    """Return service health"""
    return 'ok'


@app.route('/predict-all', methods=['GET'])
def predict_all():
    """Return predict all"""
    get_predict_all()
    
    return 'ok'


@app.route('/predict', methods=['POST'])
def predict():
    feature_dict = request.get_json()
    if not feature_dict:
        return {
            'error': 'Body is empty.'
        }, 500

    try:
        response = get_model_response(feature_dict)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
