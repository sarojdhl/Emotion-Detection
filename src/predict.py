def predict(model, data):
	'''
 		input:
 			model: machine learning model
 			data : data for which model need to predict 

 		return: 
 			prediction:  predicted output

	'''
	prediction = model.predict(data)
	return prediction