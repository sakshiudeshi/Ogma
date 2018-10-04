import API_KEYS
import json
import requests

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"


def getKey(item):
    return item[1]

response = requests.post('https://api.uclassify.com/v1/uclassify/iab-taxonomy/classify', \
    data = "{\"texts\": [\"" + sentence +"\"]}", \
    headers = {'Authorization': 'Token ' + API_KEYS.UCLASSIFY_API_KEY_READ})

response_dict = json.loads(response.content)[0]
response_list = []
for item in response_dict["classification"]:
    response_list.append([str(item["className"]), float(item["p"])])

print sorted(response_list, key=getKey, reverse=True)