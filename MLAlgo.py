from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()
import numpy as np
import pickle
from sklearn.linear_model import SGDClassifier
#
# from sklearn.datasets import fetch_20newsgroups
# twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
#
# print twenty_train.target_names #prints all the categories
# print("\n".join(twenty_train.data[0].split("\n")[:20])) #prints first line of the first data file

with open('train.txt') as f:
    train = f.read().splitlines()

train_X = []
train_Y = []
for line in train:
    split = line.rsplit(' ', 1)
    train_X.append(split[0])
    train_Y.append(split[1])

with open('test.txt') as f:
    test = f.read().splitlines()

test_X = []
test_Y = []
for line in test:
    split = line.rsplit(' ', 1)
    test_X.append(split[0])
    test_Y.append(split[1])

# print train_X, train_Y
# print twenty_train
train_X_counts = count_vect.fit_transform(train_X)
print train_X_counts.shape

X_train_tfidf = tfidf_transformer.fit_transform(train_X_counts)
print X_train_tfidf.shape

from sklearn.naive_bayes import MultinomialNB
text_clf_svm = SGDClassifier(loss='hinge', penalty='l2',  alpha=1e-3, n_iter=5, random_state=42)

text_clf_svm.fit(X_train_tfidf, train_Y)

multinomial_NB = MultinomialNB()
multinomial_NB.fit(X_train_tfidf, train_Y)

test_X_np = np.array(test_X)
test_Y_np = np.array(test_Y)
# print test_X_np
predicted = multinomial_NB.predict(tfidf_transformer.transform(count_vect.transform(test_X)))
print predicted
print np.mean(predicted == test_Y)

# f = open('cv.pickle', 'wb')
# pickle.dump(train_X_counts, f)
# f.close()
#
# f = open('tfidf.pickle', 'wb')
# pickle.dump(X_train_tfidf, f)
# f.close()