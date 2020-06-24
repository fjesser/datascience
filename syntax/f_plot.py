#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:39:46 2020

@author: felix
"""

# %% Preparations

# import modules
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import tree

# save folder in variablex
file_folder = os.path.dirname(__file__)

# load data new transformed data
df = pd.read_csv(os.path.join(file_folder, "..",
                              "input", "hotel_bookings_FE.csv"),
                 index_col=0)  # because csv data has index column


# %% inspect data
df.info()
df.head()
df.columns

# %% Logistische Regression
log_model = LogisticRegression(random_state=0).fit(df[['cost']],
                                                   df.is_canceled)

log_model.get_params()
log_model.score(df[['cost']], df.is_canceled)
log_model.coef_
np.exp(log_model.coef_)

cnf_matrix = metrics.confusion_matrix(df.is_canceled,
                                      log_model.predict(df[['cost']]))
cnf_matrix


class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

plt.show()



# %% Decision Tree
# create a classifier instance
features = ['hotel', 'lead_time', 'arrival_date', 'adults', 'children',
            'babies', 'meal', 'country', 'market_segment',
            'distribution_channel', 'is_repeated_guest',
            'previous_cancellations', 'reserved_room_type',
            'booking_changes', 'agent', 'company', 'days_spent', 'cost']
features = ['babies', 'adults']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(df[features], df.is_canceled)

tree.plot_tree(clf)
