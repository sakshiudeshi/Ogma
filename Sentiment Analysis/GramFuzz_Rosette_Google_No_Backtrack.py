import csv
import re, random, pickle
import numpy as np
import copy
import datetime

from nltk import CFG, ChartParser, Tree

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# import textrazor_API, aylien_API
import rosette_API

import jacc_thresh

import warnings
warnings.filterwarnings("ignore",category=FutureWarning)

tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()

gramLetter = "F"
gramFileName = "Grammar " + gramLetter + ".txt"
folder_type = "Rosette uClassify Grammar " + gramLetter

f = open(gramFileName, 'r')
grammar = f.read()
f.close()
# print grammarA

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# productions = '''[S -> NP VP, NP -> Det N PP, Det -> 'an', N -> 'man', PP -> P NP, P -> 'on', NP -> Det N, Det -> 'my', N -> 'cat', VP -> VP PP, VP -> VP PP, VP -> V NP, V -> 'shot', NP -> 'Bob', PP -> P NP, P -> 'outside', NP -> Det N PP, Det -> 'an', N -> 'pajamas', PP -> P NP, P -> 'outside', NP -> 'Bob', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'pajamas', PP -> P NP, P -> 'in', NP -> Det N PP, Det -> 'my', N -> 'dog', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'cat', PP -> P NP, P -> 'by', NP -> Det N, Det -> 'an', N -> 'telescope']
# '''

# sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope" #Sentence has error
# sentence = "an dog in the man saw Bob in an dog in Bob outside an park on the elephant in my elephant in my elephant"
# sentence = "the elephant with my cat walked I with an dog outside John with a cat outside my dog with the man with my man"
# sentence = "my angry cat chased an tall snake wounded a tree ate Joe outside my log"
# sentence = "James built Stephen by a ship in an man with James by an cat with an tree with James outside Irene"
# sentence = "Steve ran the lawn by the man by Elise in Elise by my squirrel by my giraffe near a squirrel on a fish"
# sentence = "Elise viewed I with my monkey with Steve near Mark near Mark near a giraffe"
# sentence = "a babbon disabled an park outside Gary outside my owl"
# sentence = "my park inside an baboon with Nick damaged Gemma in Gemma near Gary"
# sentence = "I looked my company home on my country woman Thomas"
sentence = "Olivia looked a business Thomas Thomas week outside Thomas I by woman Olivia the home room country Alexander"
# sentence = "Holly captured the bus by the snake Holly Marcus on the pajamas"
# sentence = "I meant cat an telescope an pajamas country by Irene"
# sentence = "an baboon on I damaged my gibbon near Gary near the baboon with Gary by a baboon with Gary near Gary with the elephant with I"
# sentence = "an giraffe outside Elise went Elise outside Elise"
# sentence = "Mary walked John with an pajamas outside an man in I"
# sentence = "John wounded my elephant outside Bob by a monkey outside Mary"
iters = 200
prob_delta = 0.2

client = language.LanguageServiceClient()

jaccard_threshold = jacc_thresh.dict_jacc[folder_type]


def get_label_google(inp_text):
    print inp_text
    text = inp_text
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    score = sentiment.score
    mag = sentiment.magnitude
    print "score, mag"
    print score, mag
    print ""
    # print score
    response_list = []
    if score > 0.25:
        response_list.append(["POSITIVE", score])
    elif score < -0.25:
        response_list.append(["NEGATIVE", score])
    else:
        response_list.append(["NEUTRAL", score])
    return response_list[0]

def jaccard(a, b):
    l1 = set()
    l2 = set()

    for item in a:
        l1.add(item[0])

    for item in b:
        l2.add(item[0])

    l = l1.intersection(l2)
    return float(len(l)) / (len(l1) + len(l2) - len(l))

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
    # f = open("Split_Lines.txt", "w")
    # for line in split_lines:
    #     f.write(str(line) + " " + str(len(line)) + "\n")
    # f.close()
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

def evaluate(sentence, to_print=False):
    # return evaluate_local(sentence, to_print)
    # return evaluate_api(sentence, to_print)
    return evaluate_simple(sentence, to_print)

def evaluate_simple(sentence, to_print):
    p1 = rosette_API.get_label(sentence=sentence)
    p2 = get_label_google(sentence)

    if (p1[0] != p2[0]):
        if to_print:
            print p1, p2, sentence

        return True, p1, p2
    else:
        return False, p1, p2

# def evaluate_local(sentence, to_print):
#     sentence_list = np.array([sentence])
#     # print sentence_list
#     p1 = clf1.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
#     p2 = clf2.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
#     if (p1 != p2):
#         if to_print:
#             print p1, p2, sentence_list
#
#         return True, p1, p2
#     else:
#         return False, p1, p2


def evaluate_api_jaccard(sentence, to_print):
    p1 = rosette_API.get_label(sentence=sentence)
    p2 = get_label_google(sentence)
    jaccard_val = jaccard(p1, p2)

    if to_print:
        print jaccard_val, jaccard_val < jaccard_threshold

    if (jaccard_val < jaccard_threshold):
        return True, p1, p2
    else:
        return False, p1, p2

def evaluate_api(sentence, to_print):
    p1 = rosette_API.get_label(sentence=sentence)[0]
    p2 = get_label_google(sentence)[0]
    val = False
    print " "
    if(p1[0] != p2[0]):
        val = True, p1, p2
        if to_print:
            print "Case 1"
    elif (p1[0] == p2[0] and abs(p1[1] - p2[1]) > 0.5):
        val = True, p1, p2
        if to_print:
            print "Case 2"
    else:
        val = False, p1, p2
        if to_print:
            print "Case 3"

    print p1, p2, val
    print " "
    return val

# f = open('multinomial_NB.pickle', 'rb')
# clf1 = pickle.load(f)
# f.close()
#
#
# f = open('SVM_Text_clf.pickle', 'rb')
# clf2 = pickle.load(f)
# f.close()
#
# with open('train.txt') as f:
#     train = f.read().splitlines()
#
# train_X = []
# train_Y = []
# for line in train:
#     split = line.rsplit(' ', 1)
#     train_X.append(split[0])
#
# train_X_counts = count_vect.fit_transform(train_X)
# # print train_X_counts.shape
#
# X_train_tfidf = tfidf_transformer.fit_transform(train_X_counts)

productions = get_productions(sentence, grammar)
print productions
print ' '
prods = get_base_prods(str(productions))
dict = get_grammar_dict(grammar)
dict_keys = dict.keys()

prob_keys = [1.0/len(dict_keys)] * len(dict_keys)
print prob_keys
print ' '
print prods



error_set = set()
candidate_set = set()
sentence_values = []
latest_error_prods = prods

filename = "DataFiles/ErrorDataNoBacktrackDirected_Rosette_Google_Grammar" + gramLetter + "_Jacc_" + str(jaccard_threshold) + "_" + str(datetime.datetime.now()) + ".csv"
f = open(filename, "w")
file_writer = csv.writer(f, delimiter=',')
for i in xrange(iters):
    prod_choice = np.random.choice(dict_keys, p=prob_keys)
    prod_choice_loc = [i for i, x in enumerate(dict_keys) if x == prod_choice]
    # print prod_choice_loc

    mod = random.randint(0, len(prods) - 1)
    while prod_choice != prods[mod][0]:
        mod = random.randint(0, len(prods) - 1)

    rand = random.choice(dict[prods[mod][0]])

    current_prods = copy.deepcopy(prods)
    # Checks if generating the same sentence
    while (rand == current_prods[mod][1]):
        rand = random.choice(dict[prods[mod][0]])


    current_sentence = sentence_from_prods(current_prods)
    current_eval, current_p1, current_p2 = evaluate(current_sentence, True)

    candidate_prods = copy.deepcopy(prods)
    candidate_prods[mod][1] = rand
    candidate_sentence = sentence_from_prods(candidate_prods)
    candidate_eval, candidate_p1, candidate_p2 = evaluate(candidate_sentence, True)

    # if candidate_sentence not in candidate_set:


    candidate_set.add(candidate_sentence)

    prods = copy.deepcopy(candidate_prods)

    if (False):
        prods = copy.deepcopy(current_prods)
        # print prods
        print " "
        print current_prods, sentence_from_prods(prods)
        print "Candidate -> " + candidate_sentence, candidate_eval
        print "Current -> " + current_sentence, current_eval
        print " "
        # print ''

    sentence_values.append(candidate_eval)

    if (candidate_eval):
        error_set.add(candidate_sentence)
        latest_error_prods = candidate_prods
        # prob_keys[prod_choice_loc[0]] = max(prob_keys[prod_choice_loc[0]] - prob_delta, 0)
        # norm = [float(i) / sum(prob_keys) for i in prob_keys]
        # prob_keys = norm
    # f.write(str(len(candidate_set)) + " " + str(len(error_set)) + "\n")
    file_writer.writerow([candidate_sentence, candidate_p1, candidate_p2, candidate_eval, len(candidate_set), len(error_set), str(datetime.datetime.now().time())])



f.close()
print len(error_set)
print len(candidate_set)
print sentence_values

