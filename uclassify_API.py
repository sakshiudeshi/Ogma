import API_KEYS
import json
import requests

# sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
# sentence = "an dog in the man saw Bob in an dog in Bob outside an park on the elephant in my elephant in my elephant"


def getKey(item):
    return item[1]

def get_label(sentence):

    response = requests.post('https://api.uclassify.com/v1/uclassify/iab-taxonomy/classify', \
        data = "{\"texts\": [\"" + sentence +"\"]}", \
        headers = {'Authorization': 'Token ' + API_KEYS.UCLASSIFY_API_KEY_READ})

    response_dict = json.loads(response.content)[0]
    response_list = []
    label_set = set()

    for item in response_dict["classification"]:
        label = str(item["className"]).split('_', 1)[0].upper()
        response_list.append([label, float(item["p"])])
            # label_set.add(label)

    response_list_sorted = sorted(response_list, key=getKey, reverse=True)
    final_response_list = []
    for item in response_list_sorted:
        label = item[0]
        if not label in label_set:
            final_response_list.append(item)
            label_set.add(label)

    return final_response_list[:5]

# print get_label(sentence)