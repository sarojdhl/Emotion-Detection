from src.train_test.train_model import train
from src.train_test.test_model import test
import pickle

def model_training():
	model, score = train()

	print(score)


def model_testing(data):
	model = pickle.load( open( "../checkpoint/model/01SGD.pkl", "rb" ) )

	out = test(data, model)
	print(out)



data = ["I love my life very much. I can't believe it","I sad you to death"]

model_training()
model_testing(data)







