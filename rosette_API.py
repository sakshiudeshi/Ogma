import json

import API_KEYS


from rosette.api import API, DocumentParameters, RosetteException

# sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
sentence = "an dog in the man saw Bob in an dog in Bob outside an park on the elephant in my elephant in my elephant"

def getKey(item):
    return item[1]

def get_label(alt_url='https://api.rosette.com/rest/v1/', sentence = "Default Sentence"):

    api = API(user_key=API_KEYS.ROSETTE_API_KEY, service_url=alt_url)
    params = DocumentParameters()
    label_set = set()
    final_response_list = []
    params["content"] = sentence
    params["language"] = "eng"
    try:
        response_dict = json.loads(json.dumps(api.categories(params)))["categories"]
        response_list = []
        for item in response_dict:
            response_list.append([str(item["label"]).replace("_", " "), float(item["confidence"])])

        response_list_sorted = sorted(response_list, key=getKey, reverse=True)

        for item in response_list_sorted:
            label = item[0]
            if not label in label_set:
                final_response_list.append(item)
                label_set.add(label)

        return final_response_list[:5]
    except RosetteException as exception:
        print(exception)



# RESULT = get_label(sentence=sentence)
# print(RESULT)
