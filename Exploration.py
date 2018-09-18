from nltk import CFG, Nonterminal, grammar, corpus
from nltk.parse.generate import generate
from random import choice

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


#combined Grammar
grammarC = CFG.fromstring('''
S -> NP VP
VP -> V NP | V NP PP | VP PP
PP -> P NP
V -> "saw" | "ate" | "walked" | 'shot' | 'killed' | 'wounded'
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | 'I'
Det -> "a" | "an" | "the" | "my" | 'an' | 'my' 
N -> "man" | "dog" | "cat" | "telescope" | "park" | 'elephant' | 'pajamas' | 'cat' | 'dog'
P -> "in" | "on" | "by" | "with" | 'in' | 'outside'
''')

gr = grammarC
file = open('combined_grammar.txt', 'w')

# for sentence in generate(grammar, depth=10):
#     print(' '.join(sentence))
for i in xrange(1000):
    words = produce(gr, gr.start())
    print >>file, ' '.join(word for word in words) #+ ' ' + str('1')

# ruleset = set(rule for tree in corpus.treebank.parsed_sents()[:10]
#            for rule in tree.productions())