from nltk import CFG, Nonterminal, grammar, corpus
from nltk.parse.generate import generate
from random import choice
import sys

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

with open('errors.txt') as f:
    errors = f.read().splitlines()

#Grammar A
grammarA = CFG.fromstring('''
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with" 
''')

#Grammar B
grammarB = CFG.fromstring('''
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
V -> 'shot' | 'killed' | 'wounded'
Det -> 'an' | 'my' 
N -> 'elephant' | 'pajamas' | 'cat' | 'dog'
P -> 'in' | 'outside'
''')


f = open('combined_diff_test_2.txt', 'w')
sys.stdout = f

for i in xrange(1000):
    wordsA = produce(grammarA, grammarA.start())
    wordsB = produce(grammarB, grammarB.start())
    print ' '.join(word for word in wordsA) + ' ' + choice(errors) + ' ' + ' '.join(word for word in wordsB)