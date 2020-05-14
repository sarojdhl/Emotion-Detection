from get_clean_data import get_clean_data
from sklearn.model_selection import train_test_split
from preprocessing import preprocessing
from train import train
from predict import predict
from evaluation_score import metrics

TEST_SIZE = 0.1

train_data, target_data = get_clean_data()

preprocessed_data = preprocessing(train_data)


X_train, X_test, y_train, y_test = train_test_split(preprocessed_data, target_data, test_size = TEST_SIZE, random_state = 42)

trained_model = train(X_train, y_train)

prediction_test = predict(trained_model, X_test)

score = metrics(y_test, prediction_test)

print('test evaluation score is : ', score)





