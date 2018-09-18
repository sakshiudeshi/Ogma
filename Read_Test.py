import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import random

tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()

f = open('error_set.pickle', 'rb')
error_set = pickle.load(f)
f.close()

f = open('multinomial_NB.pickle', 'rb')
clf1 = pickle.load(f)
f.close()

with open('train.txt') as f:
    train = f.read().splitlines()

train_X = []
train_Y = []
for line in train:
    split = line.rsplit(' ', 1)
    train_X.append(split[0])

train_X_counts = count_vect.fit_transform(train_X)
# print train_X_counts.shape

X_train_tfidf = tfidf_transformer.fit_transform(train_X_counts)
# print X_train_tfidf.shape


f = open('SVM_Text_clf.pickle', 'rb')
clf2 = pickle.load(f)
f.close()

error_list = list(error_set)

count = 0

for i in xrange(1000):
    list = np.array([random.choice(error_list) + ' ' + random.choice(error_list)])
    p1 = clf1.predict(tfidf_transformer.transform(count_vect.transform(list)))

    p2 = clf2.predict(tfidf_transformer.transform(count_vect.transform(list)))
    if (p1 == p2):
        count = count + 1
        # print list
    # print p1, p2

print count