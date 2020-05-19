from src.train_test.train_model import train
from src.train_test.test_model import test
import pickle
from src.db import model_score

def model_training():
	model, score_train, score_test = train()

	# print( score_train) # Train score
	# # print( score_test) # test score
	# print(score_train["accuray"])
	# print(score_train["precision_recall_f1_score"][0])
	# print(score_train["precision_recall_f1_score"][1])
	# print(score_train["precision_recall_f1_score"][2])
	model_score(model_type = 'Train', accuracy=score_train["accuray"],precision=score_train["precision_recall_f1_score"][0] ,\
		         recall=score_train["precision_recall_f1_score"][1],f1=score_train["precision_recall_f1_score"][2])

	model_score(model_type = 'Test', accuracy=score_test["accuray"],precision=score_test["precision_recall_f1_score"][0] ,\
				recall=score_test["precision_recall_f1_score"][1],f1=score_test["precision_recall_f1_score"][2])

def model_testing(data):
	model = pickle.load( open( "../checkpoint/model/01SGD.pkl", "rb" ) )

	out = test(data, model)
	# print(out)



data = ["I love my life very much. I can't believe it","I sad you to death"]

model_training()
model_testing(data)







