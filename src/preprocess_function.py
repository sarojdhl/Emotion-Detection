

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


class Count_vector:
	def __init__(self):
		self.vectorizer = CountVectorizer()

	def fit(self, data):
		self.data = data
		vectorized = self.vectorizer.fit(self.data)
		return vectorized

	def transform(self, data):
		self.data = data
		vectorized = self.vectorizer.transform(self.data)
		return vectorized



class Tfid:
	def __init__(self):
		self.tfid = TfidfTransformer()

	def fit(self, data):
		self.data = data
		transformed = self.tfid.fit(self.data)
		return transformed

	def transform(self, vectorize):
		self.vectorize = vectorize
		transformed = self.tfid.transform(self.vectorize)
		return transformed

