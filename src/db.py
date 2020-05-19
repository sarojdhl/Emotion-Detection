import pymongo
import datetime
import pickle
import time


def conn():
    mongo = pymongo.MongoClient()
    db = mongo["emotions"]  # database name
    return db


def save_model_to_db(model, model_name,collection_name):
    #pickling the model
    pickled_model = pickle.dumps(model)
    #saving model to mongoDB
    # creating connection
    #creating database in mongodb    
    db = conn()
    #creating collection
    mycon = db[collection_name]
    info = mycon.insert_one({model_name: pickled_model, 'name': model_name, 'created_time':time.time()})
    print(info.inserted_id, ' saved with this id successfully!')
    
    details = {
        'inserted_id':info.inserted_id,
        'model_name':model_name,
        'created_time':time.time()
    }
    
    return details


def load_saved_model_from_db(model_name,collection_name):
    json_data = {}
    
    db = conn()
    #creating collection
    mycon = db[collection_name]
    data = mycon.find({'name': model_name})
    
    
    for i in data:
        json_data = i
    #fetching model from db
    pickled_model = json_data[model_name]
    
    return pickle.loads(pickled_model)



###################################
def predicted_data(message,type):
    db = conn()
    mycon = db['pred_data_msg']
    info = mycon.insert_one({message: message, 'name': type})
    print(info.inserted_id, ' saved with this id successfully!')


# def api_call_logs():

def model_score(model_type,accuracy,precision,recall,f1):

    data = {"model_type":model_type,
    "accuracy":accuracy,
    "precision":precision,
    "recall":recall,
    "f1":f1}
    db = conn()
    mycon = db['model_performance']
    info = mycon.insert_one(data)
    print(info.inserted_id, ' saved with this id successfully!')
