# the folowing script will help train on using some of the machine learning techniques

# the dataset used can be found and downloaded here:
# https://ai.stanford.edu/~amaas/data/sentiment/


# Notes of recognition:
# @InProceedings{maas-EtAl:2011:ACL-HLT2011,
#  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
#  title     = {Learning Word Vectors for Sentiment Analysis},
#  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
#  month     = {June},
#  year      = {2011},
#  address   = {Portland, Oregon, USA},
#  publisher = {Association for Computational Linguistics},
#  pages     = {142--150},
#  url       = {http://www.aclweb.org/anthology/P11-1015}
#}



from sklearn.datasets import load_files

# Some manipulation techniques
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV

# cross-validation
from sklearn.model_selection import cross_val_score

import numpy as np


#  Applying the bag of words technique 
countVect =  CountVectorizer()

# extract the training data
train_data = load_files("aclImdb/train")
text_train, y_train = train_data.data, train_data.target


# extract the testing data
test_data = load_files("aclImdb/test/")
text_test, y_test = test_data.data, test_data.target

# Bag-of-Words technique
X_train = countVect.fit(text_train).transform(text_train)

# cross-validation technique
scores = cross_val_score(LogisticRegression(), X_train, y_train, cv=5)

feature_names = countVect.fit(text_train).get_feature_names()

print("Mean cross-validation accuracy using LogisticRegression: {:.2f}".format(np.mean(scores)))

param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best cross-validation score: {:.2f}".format(grid.best_score_))
print("Best parameters: ", grid.best_params_)
