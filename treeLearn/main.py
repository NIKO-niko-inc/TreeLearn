import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pydotplus as pydotplus
import sklearn
import mglearn
from IPython.display import display
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from sklearn import tree

os.environ["PATH"] += os.pathsep + 'C:/Users/User/anaconda3/Library/bin/graphviz'

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
 cancer.data, cancer.target, stratify=cancer.target, random_state=42)
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)

print("Правильность на обучающем наборе: {:.3f}".format(tree.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(tree.score(X_test, y_test)))

export_graphviz(tree, out_file="tree.dot", class_names=["malignant", "benign"],
 feature_names=cancer.feature_names, impurity=False, filled=True)

import graphviz

with open("tree.dot") as f:
 dot_graph = f.read()
graphviz.Source(dot_graph)

mglearn.plots.plot_tree_progressive()
plt.show()

for name, score in zip(cancer["feature_names"], tree.feature_importances_):
 print(name, score)

def plot_feature_importances_cancer(model):
 n_features = cancer.data.shape[1]
 plt.barh(range(n_features), model.feature_importances_, align='center')
 plt.yticks(np.arange(n_features), cancer.feature_names)
 plt.xlabel("Важность признака")
 plt.ylabel("Признак")
plot_feature_importances_cancer(tree)

plt.show()

