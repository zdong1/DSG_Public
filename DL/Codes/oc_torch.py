# -*- coding: utf-8 -*-
"""
A Simple Torch Starter
Note: For confidentiality reasons, key fields have been removed. This originates from my response to a DS
Challenge, where the key classified label is at column [-1]. Adjust it for your case.
Multilayer perceptron model, 5 hidden layers; ReLu+ SGD Optimizer, CCE Loss Functions
Jason (Zhihang) Dong
input layer : 16 neuron, represents the feature of x, y and z
hidden layer : 5 neuron, activation using ReLU
output layer : 3 neuron, represents the label classes
optimizer = stochastic gradient descent with no batch-size
loss function = categorical cross entropy
learning rate = 0.01
epoch = 500
"""

import torch
import pandas as pd
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
torch.manual_seed(10086)



train_df = pd.read_csv("your_train.csv")
train_df.set_value(train_df['label'] == 1, ['label'],0)
train_df.set_value(train_df['label'] == 2, ['label'],1)
train_df.set_value(train_df['label'] == 3, ['label'],2)
from sklearn.cross_validation import train_test_split
X, y = train_df.iloc[:, 0:-1].values, train_df.iloc[:, -1].values

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0)


#hyperparameters
hl = 5 # number of hidden layers
lr = 0.01 # learning rate
num_epoch = 500 # epoch

#build model
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(16, hl)
        self.fc2 = nn.Linear(hl, 3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
net = Net()

#choose optimizer and loss function
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=lr)

#train
for epoch in range(num_epoch):
    X = Variable(torch.Tensor(X_train).float())
    Y = Variable(torch.Tensor(y_train).long())

    #feedforward - backprop
    optimizer.zero_grad()
    out = net(X)
    loss = criterion(out, Y)
    loss.backward()
    optimizer.step()

    if (epoch) % 50 == 0:
        print ('Epoch [%d/%d] Loss: %.4f'
                   %(epoch+1, num_epoch, loss.data[0]))

#get prediction
X = Variable(torch.Tensor(X_test).float())
Y = torch.Tensor(y_test).long()
out = net(X)
_, predicted = torch.max(out.data, 1)

#get accuration
print('Accuracy of the network %.3f %%' % (torch.sum(Y==predicted)/38829*100/0.3))
