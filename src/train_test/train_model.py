from src.data.get_clean_data import get_clean_data, data_aug
from sklearn.model_selection import train_test_split
from src.preprocessing.preprocessing import preprocessing
from src.evaluation_score import metrics
from sklearn.linear_model import SGDClassifier
import pickle
from src.db import *

TEST_SIZE = 0.2
MAX_ITER = 5
LEARNING_RATE = 1e-3

def train():

	'''
	 	return: 
	 		model: trained machine learning model
	 		score: metrics score of ML model
	'''
	data = get_clean_data()
	train_data, target_data = data_aug(data)

	preprocessed_data= preprocessing.train_preprocessing(train_data)


	X_train, X_test, y_train, y_test = train_test_split(preprocessed_data, target_data, test_size = TEST_SIZE, random_state = 42, shuffle = True)

	print("\n X_train" ,X_train)

	model = SGDClassifier(loss='modified_huber', penalty='l2', alpha = LEARNING_RATE, random_state=2020,max_iter = MAX_ITER, tol=None)

	model.fit(X_train, y_train)
#
	pickled_model  = pickle.dump(model, open('../checkpoint/model/01SGD.pkl', 'wb'))
	details = save_model_to_db(model = model, model_name = 'SGD_clf',collection_name="model")
	print(details)
#

	# Load model from database 
	model = load_saved_model_from_db(model_name = 'SGD_clf',collection_name="model")
	prediction_test = model.predict(X_test)
	prediction_train = model.predict(X_train)

	score_train = metrics(y_train, prediction_train)
	score_test = metrics(y_test, prediction_test)


	return (model, score_train, score_test)


