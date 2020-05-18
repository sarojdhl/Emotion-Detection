from src.data.get_clean_data import get_clean_data
from sklearn.model_selection import train_test_split
from src.preprocessing.preprocessing import preprocessing
from src.evaluation_score import metrics
from sklearn.linear_model import SGDClassifier
import pickle


TEST_SIZE = 0.1
MAX_ITER = 200
LEARNING_RATE = 1e-3

def train():

	'''
	 	return: 
	 		model: trained machine learning model
	 		score: metrics score of ML model
	'''

	train_data, target_data = get_clean_data()

	preprocessed_data, fit, fit1 = preprocessing.train_preprocessing(train_data)


	X_train, X_test, y_train, y_test = train_test_split(preprocessed_data, target_data, test_size = TEST_SIZE, random_state = 42)

	model = SGDClassifier(loss='modified_huber', penalty='l2', alpha = LEARNING_RATE, random_state=42,max_iter = MAX_ITER, tol=None)

	model.fit(X_train, y_train)

	pickle.dump(model, open('../checkpoint/model/01SGD.pkl', 'wb'))
	

	prediction_test = model.predict(X_test)

	score = metrics(y_test, prediction_test)

	return (model, score)

	


