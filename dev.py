import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import plasma
from plasma import utils
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score
import graphviz

app = plasma.App()

data = app.datasets[0]

x_cols = ['Time',
          'Amount',
          'V1',
          'V2',
          'V3',
          'V4',
          'V5',
          'V6',
          'V7',
          'V8',
          'V9',
          'V10',
          'V11',
          'V12',
          'V13',
          'V14',
          'V15',
          'V16',
          'V17',
          'V18',
          'V19',
          'V20',
          'V21',
          'V22',
          'V23',
          'V24',
          'V25',
          'V26',
          'V27',
          'V28']

y_cols = ['Class']

train_data, val_data, test_data = utils.preprocess_data(data,
                                                        cols=[x_cols,y_cols],
                                                        split_config=[.8,.1,.1],
                                                        pos_split_config=[.8,.1,.1],
                                                        pre_shuffle=False,
                                                        norm_scale_on=False,
                                                        to_numpy=False,
                                                        debug_on=True)




# print('')
# utils.counts_check(datasets,y_cols[0])
#
# train_data = datasets['train']
# test_data = datasets['test']
#
# fraud_tree = tree.DecisionTreeClassifier()
#
# fraud_tree = fraud_tree.fit(train_data.x,train_data.y)
#
#
# dot_data = tree.export_graphviz(fraud_tree, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("fraud")
#
#
# def print_stats(y_hat, y_true):
#     print("Accuracy = {}".format(accuracy_score(y_true, y_hat)))
#     print("Precision = {}".format(precision_score(y_true, y_hat)))
#     print("Recall = {}".format(recall_score(y_true, y_hat)))
#
#
# preds = fraud_tree.predict(test_data.x)
#
# print_stats(preds,test_data.y)
#
#

#
# train_data, val_data, test_data  = utils.preprocess_data(data,
#                                                          cols=[selected_features,y_cols],
#                                                          split_config=[.8, .1, .1],
#                                                          pos_split_config=None,
#                                                          pre_shuffle=True,
#                                                          to_numpy=False,
#                                                          pos_dist=False,
#                                                          random_state=random_state,
#                                                          debug_on=True).values()
