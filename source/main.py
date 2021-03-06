import numpy as np
from neural_network import *
import pandas as pd

def main():
	# Importing the dataset
	dataset = pd.read_csv('/home/leo/Documents/Extra/Git-Github-Python-POO-Neural-Nets/Churn_Modelling.csv')
	X = dataset.iloc[:, 3:13].values
	y = dataset.iloc[:, 13].values

	# Encoding categorical data
	from sklearn.preprocessing import LabelEncoder, OneHotEncoder
	labelencoder_X_1 = LabelEncoder()
	X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
	labelencoder_X_2 = LabelEncoder()
	X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
	onehotencoder = OneHotEncoder(categorical_features = [1])
	X = onehotencoder.fit_transform(X).toarray()
	X = X[:, 1:]

	# Splitting the dataset into the Training set and Test set
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	y_train = np.array(y_train, dtype = float).reshape((y_train.shape[0],1))
	y_test = np.array(y_test, dtype = float).reshape((y_test.shape[0], y_train.shape[1]))
	
	# Creating the NN architeture
	nn = NeuralNetwork()
	nn.add(Layer(6, 11))
	nn.add(Layer(1, 6))
	
	# Training and validating
	nn.train(X_train, y_train, 0.01, 100)
		
	nn.predict(X_test, y_test)
	y_pred = nn.predict(X_test, y_test)

	y_pred = np.round(y_pred)
	nn.score(y_test, y_pred)	
	
if __name__ == '__main__':
	main()