from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def metrics(actual, pred):
	'''
 		input:
 			actual: actual output value
 			pred  : predicted output value

 		return: 
 			metric: dictionary with accuracy score, precision_recall_f1 score

	'''
	accuracy = accuracy_score(actual, pred)
	precision_recall_f1score = precision_recall_fscore_support(actual, pred, average='micro')
	metric = {'accuray': accuracy, 'precision_recall_f1_score': precision_recall_f1score}
	return metric
