# -*- coding: utf-8 -*-
"""
Zillow Data Scientist Challenge
XG Boost Simple
Jason (Zhihang) Dong
"""

import pandas as pd
import seaborn as sns
import numpy as np
# Set up the Dataset
color = sns.color_palette() # Set a bit more colors
train_df = pd.read_csv("training_CONFIDENTIAL.csv", parse_dates=["TransDate"])
test_df = pd.read_csv("test_CONFIDENTIAL.csv", parse_dates=["TransDate"])
# train_df = pd.get_dummies(train_df, prefix=['County']) This does not help: we did not find
# independent non-described county effect.
train_df['Latitude'] = train_df.Latitude/1e6
train_df['Longitude'] = train_df.Longitude/1e6
train_df_new = train_df.fillna(0, inplace=True)
train_df[['BGMedIncome','LotSizeSquareFeet']]=train_df[['BGMedIncome','LotSizeSquareFeet']].astype(float)
x_train = train_df.iloc[:, np.r_[6:11, 12, 14:16, 21]].values
y_train = train_df['SaleDollarCnt'].values
test_df['Latitude'] = test_df.Latitude/1e6
test_df['Longitude'] = test_df.Longitude/1e6
test_df_new = test_df.fillna(0, inplace=True)
test_df[['BGMedIncome','LotSizeSquareFeet']]=test_df[['BGMedIncome','LotSizeSquareFeet']].astype(float)
x_test = test_df.iloc[:, np.r_[6:11, 12, 14:16, 21]].values
y_test = test_df['SaleDollarCnt'].values



import xgboost as xgb
y_mean = np.mean(y_train)

xgb_params = {
    'eta': 0.02,
    'max_depth': 6,
    'subsample': 0.60,
    'objective': 'reg:linear',
    'eval_metric': 'mae',
    'base_score': y_mean,
    'silent': 1
}

dtrain = xgb.DMatrix(x_train, y_train)
dtest = xgb.DMatrix(x_test)

# cross-validation
cv_result = xgb.cv(xgb_params,
                   dtrain,
                   nfold=10,
                   num_boost_round=500,
                   early_stopping_rounds=5,
                   verbose_eval=10,
                   show_stdv=False
                  )
num_boost_rounds = len(cv_result)
print(num_boost_rounds)
# train model
model = xgb.train(dict(xgb_params, silent=1), dtrain, num_boost_round=num_boost_rounds)
pred = model.predict(dtest)
y_pred =[]

for i, predict in enumerate(pred):
    y_pred.append(str(round(predict,4)))
y_pred = np.array(y_pred)

output = pd.DataFrame({'PropertyID': test_df['PropertyID'].astype(np.int32),
        'Predicted': y_pred})

# set col 'PropertyID' to first col
cols = output.columns.tolist()
cols = cols[-1:] + cols[:-1]
output = output[cols]

from datetime import datetime
output.to_csv('Result{}.csv'.format(datetime.now().strftime('%Y%m%d_%H%M%S')), index=False)
