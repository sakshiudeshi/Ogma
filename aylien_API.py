from aylienapiclient import textapi
import API_KEYS
import json

sentence_test = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"

def get_label(sentence):
    client = textapi.Client(API_KEYS.AYLIEN_APP_ID, API_KEYS.AYLIEN_KEY)
    response = client.ClassifyByTaxonomy({'text': sentence, 'taxonomy': 'iab-qag', 'language':'en'})
    # print response['categories'][0]['label']
    labels = []
    for categories in response["categories"]:
        labels.append([(categories["label"]).encode('utf-8').upper(), float(categories["score"])])

    return labels[:5]

# print get_label(sentence_test)
