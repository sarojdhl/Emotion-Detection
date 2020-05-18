import re
from nltk.corpus import stopwords
import nltk

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
        
def get_value(text):
	'''
		input:
			text: text to be cleaned

	 	return: 
	 		text: cleaned text
	 		
	'''



	text = text.lower()
	# replace REPLACE_BY_SPACE_RE symbols by space in text
	text = REPLACE_BY_SPACE_RE.sub(' ', text)
	# delete symbols which are in BAD_SYMBOLS_RE from text
	text = BAD_SYMBOLS_RE.sub('', text)
	# delete stopwors from text
	text = ' '.join(word for word in text.split() if word not in STOPWORDS)
	return text
        
        

        


