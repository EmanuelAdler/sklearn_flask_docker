from flask import Flask
import joblib
from sklearn.ensemble import RandomForestClassifier


# Initialize App
app = Flask(__name__)

# Load models
model = joblib.load('model/mlp.joblib')
