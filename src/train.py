from sklearn.linear_model import SGDClassifier

MAX_ITER = 5
LEARNING_RATE = 1e-3

def train(x, y):
	model = SGDClassifier(loss='hinge', penalty='l2', alpha = LEARNING_RATE, random_state=42,max_iter = MAX_ITER, tol=None)

	model.fit(x, y)
	return model


