
import pickle
from src.data.clean_data import get_value


def test(data, model):
	'''
	 	input:
	 		data: data that needs to be test on model
	 		model: machine learning model

	 	return: 
	 		output: prediction of data using model
	'''

	cleaned_data = [get_value(msg) for msg in data]
	# print(cleaned_data)

	preprocessor = pickle.load( open( "../checkpoint/preprocessor/preprocessor.pkl", "rb" ) )
	

	out_vect = preprocessor.transform(cleaned_data)
	
	output = model.predict(out_vect)
	return output

