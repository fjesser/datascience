#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:39:46 2020

@author: felix
"""

# %% Preparations

# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# save folder in variablex
file_folder = os.path.dirname(__file__)

# load data new transformed data
df = pd.read_csv(os.path.join(file_folder, "..",
                              "input", "hotel_bookings_FE.csv"),
                 index_col=0)  # because csv data has index column


# %% inspect data
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

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

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