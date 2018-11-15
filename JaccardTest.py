import uclassify_API, rosette_API

# sentence = "the elephant with my cat walked I with an dog outside John with a cat outside my dog with the man with my man"
# sentence = "I ate Mary with Mary"
# sentence = "a cat in a dog wounded Bob outside an telescope by I outside my dog outside a telescope with an dog outside a telescope" # Jaccard index 1 sentence
# sentence = "Wayne ate the little angry tall tree outside a frightened bear"
sentence = "my angry cat chased a tall snake wounded a tree ate Joe outside my log"
# l1 = [['SPORTS', 0.508389], ['ARTS AND ENTERTAINMENT', 0.289764], ['PETS', 0.13624], ['NON STANDARD CONTENT', 0.0100388], ['HEALTH AND FITNESS', 0.00796675]]
# l2 = [['TRAVEL', 0.23621088], ['HEALTH AND FITNESS', 0.10447168], ['PETS', 0.10377311], ['SPORTS', 0.06433649], ['AUTOMOTIVE', 0.06146078]]


# l1 = [['SPORTS', 0.508389], ['ARTS AND ENTERTAINMENT', 0.289764], ['PETS', 0.13624], ['NON STANDARD CONTENT', 0.0100388], ['HEALTH AND FITNESS', 0.00796675], ['FOOD AND DRINK', 0.00146825], ['FAMILY AND PARENTING', 0.00138488], ['HOBBIES AND INTERESTS', 0.000651221], ['TRAVEL', 0.000247485], ['SHOPPING', 0.000155783], ['RELIGION AND SPIRITUALITY', 0.000122985], ['LAW AND GOVERNMENT AND POLITICS', 8.99617e-05], ['STYLE AND FASHION', 6.14494e-05], ['SCIENCE', 4.40559e-05], ['ILLEGAL CONTENT', 3.44116e-05], ['SOCIETY', 6.885e-06], ['HOME AND GARDEN', 6.68381e-06], ['CAREERS', 3.87713e-06], ['REAL ESTATE', 1.85269e-06], ['EDUCATION', 1.42981e-06], ['TECHNOLOGY AND COMPUTING', 9.34894e-07], ['AUTOMOTIVE', 7.72144e-07], ['BUSINESS', 4.74384e-07], ['PERSONAL FINANCE', 3.49499e-07]]
# l2 = [['TRAVEL', 0.23621088], ['HEALTH AND FITNESS', 0.10447168], ['PETS', 0.10377311], ['SPORTS', 0.06433649], ['AUTOMOTIVE', 0.06146078], ['EDUCATION', 0.03763975], ['ARTS AND ENTERTAINMENT', 0.03155895], ['HOBBIES AND INTERESTS', 0.01917924], ['BUSINESS', -0.01215032], ['RELIGION AND SPIRITUALITY', -0.07790571], ['CAREERS', -0.09643124], ['SOCIETY', -0.0983898], ['REAL ESTATE', -0.09978187], ['LAW GOVERNMENT AND POLITICS', -0.10695791], ['SCIENCE', -0.12802415], ['FAMILY AND PARENTING', -0.12980766], ['HOME AND GARDEN', -0.17296281], ['STYLE AND FASHION', -0.19986463], ['FOOD AND DRINK', -0.20343753], ['PERSONAL FINANCE', -0.20574936], ['TECHNOLOGY AND COMPUTING', -0.23775947]]



def jaccard(a, b):
    l1 = set()
    l2 = set()

    for item in a:
        l1.add(item[0])

    for item in b:
        l2.add(item[0])

    l = l1.intersection(l2)
    return float(len(l)) / (len(l1) + len(l2) - len(l))

def evaluate_api_jaccard(sentence, to_print):
    p1 = rosette_API.get_label(sentence=sentence)
    p2 = uclassify_API.get_label(sentence)
    jaccard_val = jaccard(p1, p2)

    if to_print:
        print jaccard_val, jaccard_val < 0.3, p1, p2

    return jaccard_val < 0.3, p1, p2


# p1 = rosette_API.get_label(sentence=sentence)
# p2 = uclassify_API.get_label(sentence)
# print jaccard(p1, p2)

print evaluate_api_jaccard(sentence, True)
