#!/usr/bin/python

"""
A Cost-Sensitive Softmax Multi-Class Classification Model using Downsampling
Max Depth = 6
learning rate = 0.01
epoch = 500
Note: for confidentiality reasons, key variables have been removed. In this example,
classified labels are in column [-1]
"""


from __future__ import division
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import itertools
import matplotlib as plt


train_df = pd.read_csv("your_train.csv")
X = train_df.ix[:, train_df.columns != 'label']
y = train_df.ix[:, train_df.columns == 'label']

# Number of data points in the  label 3
number_records_third = len(train_df[train_df.label == 3])
third_indices = np.array(train_df[train_df.label == 3].index)

# Picking the indices of the label 1 & 2
first_indices = train_df[train_df.label == 1].index
second_indices = train_df[train_df.label == 2].index
# Out of the indices we picked, randomly select "x" number
random_first_indices = np.random.choice(first_indices, 10*number_records_third, replace = False)
random_first_indices = np.array(random_first_indices)

random_second_indices = np.random.choice(second_indices, 2*number_records_third, replace = False)
random_second_indices = np.array(random_second_indices)

# Appending the 2 indices
under_sample_indices = np.concatenate([third_indices,random_first_indices,
                                       random_second_indices])

# Under sample dataset
under_sample_data = train_df.iloc[under_sample_indices,:]

X_undersample = under_sample_data.ix[:, under_sample_data.columns != 'label']
y_undersample = under_sample_data.ix[:, under_sample_data.columns == 'label']

# Showing ratio
print("Percentage of Label 1: ", len(under_sample_data[under_sample_data.label == 1])/len(under_sample_data))
print("Percentage of Label 2: ", len(under_sample_data[under_sample_data.label == 2])/len(under_sample_data))
print("Percentage of Label 3: ", len(under_sample_data[under_sample_data.label == 3])/len(under_sample_data))
print("Total number of transactions in resampled data: ", len(under_sample_data))


X, y = X_undersample.values, y_undersample.values
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0)

xg_train = xgb.DMatrix(X_train, label=y_train)
xg_test = xgb.DMatrix(X_test, label=y_test)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.01
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 4

watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 50
bst = xgb.train(param, xg_train, num_round, watchlist)
# get prediction
pred = bst.predict(xg_test)
print(pred)
error_rate = np.sum(pred != y_test) / y_test.shape[0]
print('Test error using softmax = {}'.format(error_rate))

# do the same thing again, but output probabilities
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist)
pred_prob = bst.predict(xg_test).reshape(y_test.shape[0], 4)
pred_label = np.argmax(pred_prob, axis=1)
error_rate = np.sum(pred_label != y_test) / y_test.shape[0]
print('Test error using softprob = {}'.format(error_rate))

# Finally, on our test set
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.05
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 4

test_df = pd.read_csv("your_test.csv")
ts_x = test_df.values
xg_ts = xgb.DMatrix(ts_x)
watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 50
bst = xgb.train(param, xg_train, num_round, watchlist)
# get prediction
ts_pred = bst.predict(xg_ts)
ts_pred = ts_pred.astype(np.int64)
print(ts_pred)
np.savetxt("predicted_labels_3.csv", ts_pred, delimiter=",")


from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.metrics import confusion_matrix,precision_recall_curve,auc,roc_auc_score,roc_curve,recall_score,classification_report


# ROC CURVE
lr = LogisticRegression(C = 0.01, penalty = 'l1')
y_pred_undersample_score = lr.fit(X_train,y_train.ravel()).decision_function(X_test)

# You can plot ROC using this code, but you must binarize the outcomes...

# fpr, tpr, thresholds = roc_curve(y_test.ravel(),y_pred_undersample_score)
# roc_auc = auc(fpr,tpr)
