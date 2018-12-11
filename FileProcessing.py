from math import floor
from random import shuffle


def get_training_and_testing_sets(list):
    shuffle(list)
    split = 0.8
    split_index = int(floor(len(list) * split))
    training = list[:split_index]
    testing = list[split_index:]
    return training, testing

with open('corpus_for_retraining.txt') as f:
    lines = f.read().splitlines()

train = open('train_re.txt', 'w')
test = open('test_re.txt', 'w')

training, testing = get_training_and_testing_sets(lines)

for i in training:
    print>>train, i

for i in testing:
    print>>test, i