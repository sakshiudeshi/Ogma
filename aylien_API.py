from aylienapiclient import textapi
import API_KEYS
import json

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"

def get_labels(senttence):
    client = textapi.Client(API_KEYS.AYLIEN_APP_ID, API_KEYS.AYLIEN_KEY)
    response = client.ClassifyByTaxonomy({'text': sentence, 'taxonomy': 'iab-qag'})
    # print response['categories'][0]['label']
    labels = []
    for categories in response["categories"]:
        labels.append([str(categories["label"]), float(categories["score"])])

    return labels

# print get_labels(sentence)