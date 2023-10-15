import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from ms import model


def predict(X, model):
    prediction = model.predict(X)[0]
    print(model.predict(X))
    return prediction


def get_model_response(json_data):
    X = pd.DataFrame.from_dict(json_data)
    print(X)
    prediction = predict(X, model)
    if prediction == 1:
        label = "Potable"
    else:
        label = "Not Potable"
    return {
        'status': 200,
        'label': label,
        'prediction': int(prediction)
    }


def get_predict_all():
    test_df = pd.read_pickle("model/test_df.pkl")
    test_expect = pd.read_pickle("model/test_expect.pkl")
    y_pred = model.predict(test_df)
    print(test_expect)
    print(y_pred)
    print(accuracy_score(test_expect, y_pred))
    print(precision_score(test_expect, y_pred))
    print(recall_score(test_expect, y_pred))
    print(f1_score(test_expect, y_pred))
    