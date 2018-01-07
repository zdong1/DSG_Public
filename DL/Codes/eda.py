# -*- coding: utf-8 -*-
"""
Zillow Data Scientist Challenge
Exploratory Data Analysis
Jason (Zhihang) Dong
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Dataset
color = sns.color_palette() # Set a bit more colors
train_df = pd.read_csv("training_CONFIDENTIAL.csv", parse_dates=["TransDate"])
print(train_df.head())

# See if there is any repetitive records
print(train_df['PropertyID'].value_counts().reset_index()['PropertyID'].value_counts())
# Transfer the Long/Lat into the correct scale
train_df['Latitude'] = train_df.Latitude/1000000
train_df['Longitude'] = train_df.Longitude/1000000

print(train_df.head())

# Plot the Housing Price
plt.figure(figsize=(8,6))
hp = plt.hist(train_df.SaleDollarCnt, bins = 20, color= "pink")
plt.show()

# Check if there is any seasonality in the amount of transactions
train_df['TransMonth'] = train_df['TransDate'].dt.month
cnt_srs = train_df['TransMonth'].value_counts()
plt.figure(figsize=(12,6))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8, color="darkgreen")
plt.xticks(rotation='vertical')
plt.xlabel('Month of transaction', fontsize=12)
plt.ylabel('Transaction Amount', fontsize=12)
plt.show()


# Check Missing Data
missing_df = train_df.isnull().sum(axis=0).reset_index()
missing_df.columns = ['column_name', 'missing_count']
missing_df = missing_df.ix[missing_df['missing_count']>0]
missing_df = missing_df.sort_values(by='missing_count')

ind = np.arange(missing_df.shape[0])
width = 0.9
fig, ax = plt.subplots(figsize=(12,14))
rects = ax.barh(ind, missing_df.missing_count.values, color='blue')
ax.set_yticks(ind)
ax.set_yticklabels(missing_df.column_name.values, rotation='horizontal')
ax.set_xlabel("Count of missing values")
ax.set_title("Number of missing values in each column")
plt.show()

# Wow... the missing data is really trivial, so the data are in really good quality.


# See how sales are distributed over the map
sns.jointplot(x=train_df.Latitude.values, y=train_df.Longitude.values, kind="kde")
plt.ylabel('Longitude')
plt.xlabel('Latitude')
plt.show()

# Or a fancier one...
f, ax = plt.subplots(figsize=(10, 10))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(train_df.Latitude, train_df.Longitude, cmap=cmap, n_levels=60, shade=True)
plt.show();


# Now check out some correlations in the variables we use
train_df_new = train_df.fillna(0, inplace=True)

# Picking up meaningful variables only (block no.s does not make sense)
var_cols = [col for col in train_df.columns if col not in ['SaleDollarCnt'] if train_df[col].dtype=='float64']
print(var_cols)
labels = []
values = []
for col in var_cols:
    labels.append(col)
    values.append(np.corrcoef(train_df[col].values, train_df.SaleDollarCnt.values)[0,1])
corr_df = pd.DataFrame({'col_labels':labels, 'corr_values':values})
corr_df = corr_df.sort_values(by='corr_values')

var_sel = corr_df.ix[(corr_df['corr_values']>0.1) | (corr_df['corr_values'] < -0.1)]
print(var_sel)

# Figure out a smaller, more important subset

cols_to_use = var_sel.col_labels.tolist()
temp_df = train_df[cols_to_use]
corrmat = temp_df.corr(method='spearman')
f, ax = plt.subplots(figsize=(24, 24))

# Draw the heatmap using seaborn
sns.heatmap(corrmat, vmax=1., square=True, cmap="YlGnBu")
plt.title("Important variables correlation map", fontsize=24)
plt.show()

# Feature Extraction using xgboost!

import xgboost as xgb
xgb_params = {
    'eta': 0.05,
    'max_depth': 8,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'objective': 'reg:linear',
    'silent': 1,
    'seed' : 0
}

train_y = train_df['SaleDollarCnt'].values
train_df = train_df.drop(['PropertyID', 'SaleDollarCnt', 'TransDate','censusblockgroup',
                          'ZoneCodeCounty','Usecode'], axis=1)


dtrain = xgb.DMatrix(train_df, train_y, feature_names=train_df.columns.values)
model = xgb.train(dict(xgb_params, silent=0), dtrain, num_boost_round=50)

# plot the important features
fig, ax = plt.subplots(figsize=(12,18))
xgb.plot_importance(model,  height=0.8, ax=ax)
plt.show()
