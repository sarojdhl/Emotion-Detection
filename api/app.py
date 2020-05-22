import sys
sys.path.append("..")
from flask import abort
from flask import make_response, jsonify
from flask import Flask, request, render_template
from flask_restful import Api, Resource
app = Flask(__name__)
apis = Api(app)
import numpy as np
from src.preprocessing.preprocessing import preprocessing
#from src.db import load_saved_model_from_db
import pickle
from src.data.clean_data import get_value



def predict_type(msg):
    print("Message inpredict_type: ", msg)
    # Call a model to predict message
    model  = pickle.load(open('../checkpoint/model/01SGD.pkl', 'rb'))  
    # mess = list(msg)
    # print(type(mess))
    cleaned_data = [get_value(msg)]
    # Load preprocessor from db
    preprocessor = pickle.load(open('../checkpoint/preprocessor/preprocessor.pkl','rb'))

    out_vect = preprocessor.transform(cleaned_data)

    output = model.predict(out_vect)
    print("#################  Output ##################",output)
    return output



@app.route('/', methods=['POST','GET'])
def home():
    print(request.method)
    if  request.method == 'GET':
        return render_template('input.htm')

    else:
        name = request.form.get('usrname')# get username
        msg = request.form.get('comment')
        print(name)
        print(msg)
        predicted_emotion = predict_type(msg)
        output = {"Message": msg, "Emotion": predicted_emotion[0]}
        print (output)
        #predicted_data(msg,predicted_emotion[0])
        return render_template('output.htm',data=output["Message"], emotion=output["Emotion"])


if __name__ == "__main__":
    app.run(debug=True)
