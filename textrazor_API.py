import textrazor
import API_KEYS
textrazor.api_key = API_KEYS.TEXTRAZOR_API_KEY

def get_labels(sentence):
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    client.set_classifiers(["textrazor_iab_content_taxonomy"])
    response = client.analyze(sentence)
    labels = []

    for category in response.categories():
        # print category.query
        labels.append([str(category.label), float(category.score)])

    return labels


print get_labels("an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope")