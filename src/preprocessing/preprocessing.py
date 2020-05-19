from src.preprocessing.preprocess_function import Count_vector, Tfid
from sklearn.pipeline import make_pipeline
import pickle
from src.db import *

class preprocessing:
	def __init__(self):
		pass

	def train_preprocessing(train_data):
		'''
			input:
				train_data: data that needs to preprocessed

			return: 
				vectorized: preprocessed data
		'''

		count_vect = Count_vector()
		tfid = Tfid()
		pipe = make_pipeline(count_vect.initial(), tfid.initial())
		fit = pipe.fit(train_data)
		pickle.dump(fit, open('../checkpoint/preprocessor/preprocessor.pkl', 'wb'))
	# save in databae
		details = save_model_to_db(model = fit, model_name = 'preprocessor',collection_name="prep")
		print(details)

		vectorized = pipe.transform(train_data)
		return vectorized


	




