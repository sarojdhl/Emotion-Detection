

from src.data.clean_data import Clean_data
import pandas as pd
from src.config import DATA_PATH, DATASET
import os

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
	ob = Clean_data() # call clean data class to clean data in dataframe
	df1['message'] = df1['message'].apply(lambda msg: ob.get_value(msg)) # call get_value to clean data fraom special strings
	return (df1.message, df1.emotions)

