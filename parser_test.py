from nltk import CFG, ChartParser, Tree

grammarA = CFG.fromstring('''
S -> NP VP
VP -> V NP | V NP PP | VP PP
PP -> P NP
V -> "saw" | "ate" | "walked" | 'shot' | 'killed' | 'wounded'
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | 'I'
Det -> "a" | "an" | "the" | "my" | 'an' | 'my' 
N -> "man" | "dog" | "cat" | "telescope" | "park" | 'elephant' | 'pajamas' | 'cat' | 'dog'
P -> "in" | "on" | "by" | "with" | 'in' | 'outside'
''')


# #Grammar A
# grammarA = CFG.fromstring('''
# S -> NP VP
# VP -> V NP | V NP PP
# PP -> P NP
# V -> "saw" | "ate" | "walked"
# NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
# Det -> "a" | "an" | "the" | "my"
# N -> "man" | "dog" | "cat" | "telescope" | "park"
# P -> "in" | "on" | "by" | "with"
# ''')

# #Grammar B
# grammarB = CFG.fromstring('''
# S -> NP VP
# PP -> P NP
# NP -> Det N | Det N PP | 'I'
# VP -> V NP | VP PP
# V -> 'shot' | 'killed' | 'wounded'
# Det -> 'an' | 'my'
# N -> 'elephant' | 'pajamas' | 'cat' | 'dog'
# P -> 'in' | 'outside'
# ''')

# with open('corpus.txt') as f:
#     diff_test = f.read().splitlines()

# a = "Bob walked the telescope in John John saw Bob by a dog on my dog my dog in my elephant outside I killed an elephant I shot my pajamas in I outside an pajamas"
a = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
# a = "I killed a pajamas by Mary"
sent = a.split(' ')

print sent
parser = ChartParser(grammarA)
print parser.parse(sent)

for tree in parser.parse(sent):
    print tree, "\n\n"

t = Tree.fromstring('''(S
  (NP (Det an) (N man) (PP (P on) (NP (Det my) (N cat))))
  (VP
    (VP
      (VP (V shot) (NP Bob))
      (PP
        (P outside)
        (NP (Det an) (N pajamas) (PP (P outside) (NP Bob)))))
    (PP
      (P with)
      (NP
        (Det my)
        (N pajamas)
        (PP
          (P in)
          (NP
            (Det my)
            (N dog)
            (PP
              (P with)
              (NP
                (Det my)
                (N cat)
                (PP (P by) (NP (Det an) (N telescope))))))))))) ''')
print t.productions()
# print t.sort()