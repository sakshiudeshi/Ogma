import textrazor
import API_KEYS
textrazor.api_key = API_KEYS.TEXTRAZOR_API_KEY

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
# sentence = "James built Stephen by a ship in an man with James by an country with my tree with James outside Irene"

def get_labels(sentence):
    client = textrazor.TextRazor(extractors=["categories"])
    client.set_classifiers(["textrazor_iab_content_taxonomy"])
    response = client.analyze(sentence)
    labels = []

    category_set = set()
    for category in response.categories():
        print category.json
        category_label = str(category.label).upper().split('>')[0]
        if (category_label not in category_set):
            category_set.add(category_label)
            labels.append([category_label, float(category.score)])

    # entities = list(response.entities())
    # print entities
    return labels


# print get_labels(sentence)