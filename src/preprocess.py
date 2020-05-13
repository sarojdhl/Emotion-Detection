import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
# Count vectoriser

class Count_vector:
	def __init__(self):
		self.vectorizer = CountVectorizer()

	def fit_transform(self, data):
		self.data = data
		vectorized = self.vectorizer.fit_transform(self.data)
		return vectorized


# term frequency inverse documnt frequency
class Tfid:
	def __init__(self):
		self.tfid = TfidfTransformer()

	def fit_transform(self, vectorize):
		self.vectorize = vectorize
		transformed = self.tfid.fit_transform(self.vectorize)
		return transformed

