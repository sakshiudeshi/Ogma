from math import floor
from random import shuffle

n = 0

def get_training_and_testing_sets(list):
    shuffle(list)
    split = 0.8
    split_index = int(floor(len(list) * split))
    training = list[:split_index]
    testing = list[split_index:]
    return training, testing

with open('corpus.txt') as f:
    lines_corpus = f.read().splitlines()

with open('errors.txt') as f:
    lines_errors = f.read().splitlines()

lines = lines_errors[:n] + lines_corpus

corpus_re = open('corpus_re_' + str(n) + '.txt', 'w')

for i in lines:
    print>> corpus_re, i

train = open('train_re_' + str(n) + '.txt', 'w')
test = open('test_re_' + str(n) + '.txt', 'w')

training, testing = get_training_and_testing_sets(lines)

for i in training:
    print>>train, i

for i in testing:
    print>>test, i