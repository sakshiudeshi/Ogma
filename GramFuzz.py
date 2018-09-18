import re, random, pickle
import numpy as np

from nltk import CFG, ChartParser, Tree

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()

grammarA = '''S -> NP VP
VP -> V NP | V NP PP | VP PP
PP -> P NP
V -> "saw" | "ate" | "walked" | "shot" | "killed" | "wounded"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | "I"
Det -> "a" | "an" | "the" | "my" | "an" | "my" 
N -> "man" | "dog" | "cat" | "telescope" | "park" | "elephant" | "pajamas" | "cat" | "dog"
P -> "in" | "on" | "by" | "with" | "outside"'''

# productions = '''[S -> NP VP, NP -> Det N PP, Det -> 'an', N -> 'man', PP -> P NP, P -> 'on', NP -> Det N, Det -> 'my', N -> 'cat', VP -> VP PP, VP -> VP PP, VP -> V NP, V -> 'shot', NP -> 'Bob', PP -> P NP, P -> 'outside', NP -> Det N PP, Det -> 'an', N -> 'pajamas', PP -> P NP, P -> 'outside', NP -> 'Bob', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'pajamas', PP -> P NP, P -> 'in', NP -> Det N PP, Det -> 'my', N -> 'dog', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'cat', PP -> P NP, P -> 'by', NP -> Det N, Det -> 'an', N -> 'telescope']
# '''

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"

iters = 1000
prob_delta = 0.2

def get_productions(sentence, grammar):
    trees = []
    sent = sentence.split(' ')
    print sent
    cfgGrammar = CFG.fromstring(grammar)

    parser = ChartParser(cfgGrammar)
    for tree in parser.parse(sent):
        trees.append(str(tree).replace("\n", " "))

    # print trees[0]
    t = Tree.fromstring(trees[0])
    return t.productions()



def get_grammar_dict(grammar):
    lines = grammar.split("\n")

    quoted = re.compile('"([^"]*)"')
    split_lines = []

    for line in lines:
        split_lines.append(line.split('->'))

    line_d = {}
    for line in split_lines:
        if quoted.findall(line[1]):
            line_d[line[0].strip()] = quoted.findall(line[1])
    return line_d


# print line_d
def get_base_prods(productions):
    single_quoted = re.compile(r"'(.*?)'")
    prods = []
    for prod in productions.split(","):
        if single_quoted.findall(prod.strip()):
            p = prod.strip().split(" -> ")
            prods.append([p[0], single_quoted.findall(p[1])[0]])


    return prods

def sentence_from_prods(prods):
    list = []
    for p in prods:
        list.append(p[1])
    return " ".join(list)

def evaluate(sentence):
    sentence_list = np.array([sentence])
    # print sentence_list
    p1 = clf1.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
    p2 = clf2.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
    if (p1 != p2):
        # print p1, p2, sentence_list
        return True
    else:
        return False

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
# print train_X_counts.shape

X_train_tfidf = tfidf_transformer.fit_transform(train_X_counts)

productions = get_productions(sentence, grammarA)
print productions
print ' '
prods = get_base_prods(str(productions))
dict = get_grammar_dict(grammarA)
dict_keys = dict.keys()

prob_keys = [1.0/len(dict_keys)] * len(dict_keys)
print prob_keys
print ' '
print prods



error_set = set()

for i in xrange(iters):
    prod_choice = np.random.choice(dict_keys, p=prob_keys)
    prod_choice_loc = [i for i, x in enumerate(dict_keys) if x == prod_choice]
    # print prod_choice_loc

    mod = random.randint(0, len(prods) - 1)
    while prod_choice != prods[mod][0]:
        mod = random.randint(0, len(prods) - 1)

    rand = random.choice(dict[prods[mod][0]])
    while rand == prods[mod][1]:
        rand = random.choice(dict[prods[mod][0]])

    prods[mod][1] = rand

    candidate_sentence = sentence_from_prods(prods)
    # print candidate_sentence, evaluate(candidate_sentence)
    if (evaluate(candidate_sentence)):
        error_set.add(sentence_from_prods(prods))
        prob_keys[prod_choice_loc[0]] = max(prob_keys[prod_choice_loc[0]] - prob_delta, 0)
        norm = [float(i) / sum(prob_keys) for i in prob_keys]
        prob_keys = norm

print len(error_set)


