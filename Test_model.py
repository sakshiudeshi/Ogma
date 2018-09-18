import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()

f = open('multinomial_NB.pickle', 'rb')
clf1 = pickle.load(f)
f.close()


f = open('SVM_Text_clf.pickle', 'rb')
clf2 = pickle.load(f)
f.close()

with open('train.txt') as f:
    train = f.read().splitlines()

train_X = []
train_Y = []
for line in train:
    split = line.rsplit(' ', 1)
    train_X.append(split[0])

train_X_counts = count_vect.fit_transform(train_X)
print train_X_counts.shape

X_train_tfidf = tfidf_transformer.fit_transform(train_X_counts)
print X_train_tfidf.shape


with open('combined_grammar.txt') as f:
    diff_test = f.read().splitlines()

diff_test = np.array(diff_test)
diff_test = ["I killed a pajamas by Mary"]
diff_test = np.array(diff_test)

predicted1 = clf1.predict(tfidf_transformer.transform(count_vect.transform(diff_test)))

predicted2 = clf2.predict(tfidf_transformer.transform(count_vect.transform(diff_test)))

count = 0

file = open('combined_grammar_errors.txt', 'w')

for i in xrange(len(predicted1)):
    if(predicted1[i] != predicted2[i]):
        count = count + 1
        print >> file, diff_test[i]


print (predicted2 == predicted1)
print count