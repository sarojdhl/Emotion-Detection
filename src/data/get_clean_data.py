
from src.data.clean_data import get_value
import pandas as pd
from src.config import DATA_PATH, DATASET
import os
import random

os.chdir(DATA_PATH)
# read dataframe isear

def get_clean_data():
	'''
 		return: 
 			tuple of data that has been cleaned in (data, label) format

	'''
	df = pd.read_csv(DATASET, names=  ['index','emotions','message'])
	df1 = df.copy() # copy values to work on temp dataset
	df1.drop(columns =['index'],inplace=True)# drop column index
	 # call clean data class to clean data in dataframe
	df1['message'] = df1['message'].apply(lambda msg: get_value(msg)) # call get_value to clean data fraom special strings
	return df1

def data_aug(data):
	import random

	print ("Random number with seed 30")
	random.seed(30)
	for i in range(7446):
		spli = data.message[i].split()
		random.shuffle(spli)
		out = ' '.join(word for word in spli)
		new = pd.DataFrame([[data.emotions[i], out]], columns=['emotions', 'message'])
		data = data.append(new, ignore_index = True)
	print(data.shape)
	return (data.message, data.emotions)
	
