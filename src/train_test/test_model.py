
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
	print(cleaned_data)

	count_vect = pickle.load( open( "../checkpoint/preprocessor/coun_vect.pkl", "rb" ) )
	tfid = pickle.load( open( "../checkpoint/preprocessor/tfid.pkl", "rb" ) )

	out_vect = count_vect.transform(data)
	tfid_out = tfid.transform(out_vect)

	output = model.predict(tfid_out)
	return output

