import sys
sys.path.append("..")
from flask import abort
from flask import make_response, jsonify
from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)
apis = Api(app)
# from src.db import *
import numpy as np
from src.db import load_saved_model_from_db
from src.preprocessing.preprocessing import preprocessing
import pickle
from src.data.clean_data import get_value
# call a function to recomend


def predict_type(msg):
    print("Message inpredict_type: ", msg)
    # Call a model to predict message
    model = load_saved_model_from_db(model_name = 'SGD_clf',collection_name='model')
    # mess = list(msg)
    # print(type(mess))
    cleaned_data = [get_value(msg)]
    

    # Load preprocessor from db
    preprocessor = load_saved_model_from_db(model_name = 'preprocessor',collection_name='prep')

    out_vect = preprocessor.transform(cleaned_data)

    output = model.predict(out_vect)
    print("#################  Output ##################",output)
    return output


class Rec(Resource):
    def post(self):
        # get posted data
        data = request.get_json()
        print(data)
        msg = data['message']
        # preprocessed_data= preprocessing.train_preprocessing(msg)
        predicted_emotion = predict_type(msg)
        output = {"Message": msg, "Emotion": predicted_emotion[0]}
        return jsonify(output)




apis.add_resource(Rec, '/your_emotion')
if __name__ == "__main__":
    app.run(debug=True)
