from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def metrics(actual, pred):
	accuracy = accuracy_score(actual, pred)
	precision_recall_f1score = precision_recall_fscore_support(actual, pred, average='micro')
	metric = {'accuray': accuracy, 'precision_recall_f1_score': precision_recall_f1score}
	return metric
