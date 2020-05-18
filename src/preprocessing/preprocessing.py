from src.preprocessing.preprocess_function import Count_vector, Tfid
import pickle


class preprocessing:
	def __init__(self):
		pass

	def train_preprocessing(train_data):
		'''
	 		input:
	 			train_data: data that needs to preprocessed

	 		return: 
	 			transform: preprocessed data
		'''

		count_vect = Count_vector()
		fit = count_vect.fit(train_data)
		pickle.dump(fit, open('../checkpoint/preprocessor/coun_vect.pkl', 'wb'))
		vectorized = count_vect.transform(train_data)


		tfid = Tfid()
		fit1 = tfid.fit(vectorized)
		pickle.dump(fit1, open('../checkpoint/preprocessor/tfid.pkl', 'wb'))
		transform = tfid.transform(vectorized)

		return (transform, fit, fit1)


	




