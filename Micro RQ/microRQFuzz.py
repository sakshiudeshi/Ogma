import re, random, pickle
import numpy as np
import warnings, csv, datetime
import copy

from nltk import CFG, ChartParser, Tree

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

warnings.filterwarnings("ignore",category=FutureWarning)

tfidf_transformer = TfidfTransformer()
count_vect = CountVectorizer()

gramFileName = "Combined Grammar.txt"

f = open(gramFileName, 'r')
grammarA = f.read()
f.close()

arrs = [200]

# productions = '''[S -> NP VP, NP -> Det N PP, Det -> 'an', N -> 'man', PP -> P NP, P -> 'on', NP -> Det N, Det -> 'my', N -> 'cat', VP -> VP PP, VP -> VP PP, VP -> V NP, V -> 'shot', NP -> 'Bob', PP -> P NP, P -> 'outside', NP -> Det N PP, Det -> 'an', N -> 'pajamas', PP -> P NP, P -> 'outside', NP -> 'Bob', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'pajamas', PP -> P NP, P -> 'in', NP -> Det N PP, Det -> 'my', N -> 'dog', PP -> P NP, P -> 'with', NP -> Det N PP, Det -> 'my', N -> 'cat', PP -> P NP, P -> 'by', NP -> Det N, Det -> 'an', N -> 'telescope']
# '''

# sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
for n in arrs:
    sentence = "an elephant outside an cat killed John outside an elephant by I in an dog by an dog with the dog in a park"
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


    def evaluate(sentence, to_print=False):
        sentence_list = np.array([sentence])
        # print sentence_list
        p1 = clf1.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
        p2 = clf2.predict(tfidf_transformer.transform(count_vect.transform(sentence_list)))
        if (to_print):
            print p1, p2, p1 != p2, candidate_sentence
        return p1 != p2, p1, p2

    f = open('multinomial_NB_re_' + str(n) + '.pickle', 'rb')
    clf1 = pickle.load(f)
    f.close()

    f = open('SVM_Text_clf_re_' + str(n) + '.pickle', 'rb')
    clf2 = pickle.load(f)
    f.close()

    with open('train_re_' + str(n) + '.txt') as f:
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

    prob_keys = [1.0 / len(dict_keys)] * len(dict_keys)
    print prob_keys
    print ' '
    print prods




    print_error = False

    error_count = open('error_count_' + str(n) + '.txt', 'w')

    for i in xrange(50):
        error_set = set()
        candidate_set = set()
        sentence_values = []
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
            current_eval, current_p1, current_p2 = evaluate(current_sentence, False)

            candidate_prods = copy.deepcopy(prods)
            candidate_prods[mod][1] = rand
            candidate_sentence = sentence_from_prods(candidate_prods)
            candidate_eval, candidate_p1, candidate_p2 = evaluate(candidate_sentence, False)

            # if candidate_sentence not in candidate_set:


            candidate_set.add(candidate_sentence)

            prods = copy.deepcopy(candidate_prods)

            if (current_eval == True and candidate_eval == False):
                prods = copy.deepcopy(current_prods)
                # print prods
                if (print_error):
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

        print len(error_set)
        print>>error_count, len(error_set)

