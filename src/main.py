# Import necessary libraries
from get_clean_data import get_clean_data
from sklearn.model_selection import train_test_split
from preprocess import Count_vector, Tfid
from train import train
from predict import predict
from evaluation_score import metrics

TEST_SIZE = 0.2 # test size = 20%

# get cleanded data
data = get_clean_data()
# train data
train_data = data.message 
target_data = data.emotions # emotions as target

count_vect = Count_vector()
vectorized = count_vect.fit_transform(train_data)

tfid = Tfid()
transform = tfid.fit_transform(vectorized)
# train test split data
X_train, X_test, y_train, y_test = train_test_split(transform, target_data, test_size = TEST_SIZE, random_state = 42)
# train data
trained_model = train(X_train, y_train)
#predict
prediction_test = predict(trained_model, X_test)
# find test score
score = metrics(y_test, prediction_test)

print('test evaluation score is : ', score)







