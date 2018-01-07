# -*- coding: utf-8 -*-
"""
One Concern Data Science Challenge
Neural Network Implementation with Softmax+ReLu via Keras, SGD Optimizer
Jason (Zhihang) Dong
"""
import pandas as pd
train_df = pd.read_csv("train.csv")
train_df.set_value(train_df['label'] == 1, ['label'],0)
train_df.set_value(train_df['label'] == 2, ['label'],1)
train_df.set_value(train_df['label'] == 3, ['label'],2)
from sklearn.cross_validation import train_test_split
X, y = train_df.iloc[:, 0:-1].values, train_df.iloc[:, -1].values

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0)

"""
Multilayer perceptron model, with one hidden layer.
input layer : 16 neuron, represents the feature of the dataset
hidden layer : 10 neuron, activation using ReLU
output layer : 3 neuron, represents the labels of dataset usingSoftmax Layer
optimizer = stochastic gradient descent with no batch-size
loss function = categorical cross entropy
learning rate = default from keras.optimizer.SGD, 0.01
epoch = 500
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils

#change target format
y_train = np_utils.to_categorical(y_train)

#build model
model = Sequential()
model.add(Dense(output_dim=10, input_dim=16))
model.add(Activation("relu"))
model.add(Dense(output_dim=3))
model.add(Activation("softmax"))

#choose optimizer and loss function
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

#train
model.fit(X_train, y_train, nb_epoch=500, batch_size=120)


#get prediction
classes = model.predict_classes(X_test, batch_size=120)

#get accuration
import numpy as np
accuration = np.sum(classes == y_test)/38829 * 100

print("Test Accuration : " + str(accuration) + '%')
print("Prediction :")
print(classes)
print("Target :")
print(np.asarray(y_test,dtype="int32"))
