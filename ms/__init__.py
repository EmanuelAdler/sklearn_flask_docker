from flask import Flask
from keras.layers import Dense, Dropout, BatchNormalization
from keras.models import Sequential, load_model

# Initialize App
app = Flask(__name__)

# Load models
model = load_model('model/tf_model.keras')
