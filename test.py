import textrazor_API, aylien_API
from random import choice

from nltk import CFG, ChartParser, Tree, Nonterminal

iters = 1000

gramFileName = "toy.cfg"

f = open(gramFileName, 'r')
grammar_string = f.read()
f.close()
# print grammarA
grammar = CFG.fromstring(grammar_string)

def produce(gr, symbol):
    words = []
    productions = gr.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if not type(sym) == Nonterminal:
            words.append(sym)
        else:
            words.extend(produce(gr, sym))
    return words

for i in xrange(iters):
    wordsA = produce(grammar, grammar.start())
    candidate_sentence = ' '.join(word for word in wordsA)
    print candidate_sentence
    # print aylien_API.get_label(candidate_sentence)
    # print textrazor_API.get_labels(candidate_sentence)
    print ' '