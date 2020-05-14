from preprocess_function import Count_vector, Tfid

def preprocessing(train_data):
	'''
 		input:
 			train_data: data that needs to preprocessed

 		return: 
 			transform: preprocessed data
	'''

	count_vect = Count_vector()
	fit = count_vect.fit(train_data)
	vectorized = count_vect.transform(fit)


	tfid = Tfid()
	fit = count_vect.fit(train_data)
	transform = tfid.transform(fit)

	return transform
