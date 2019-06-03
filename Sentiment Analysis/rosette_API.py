import json

import API_KEYS


from rosette.api import API, DocumentParameters, RosetteException

# sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"
# sentence = "an dog in the man saw Bob in an dog in Bob outside an park on the elephant in my elephant in my elephant"
# sentence = "My house is on fire. Please send help in Sebastopol, CA. There is a huge forest fire approaching the town"
sentence = "I am sad"
def getKey(item):
    return item[1]

def get_label(alt_url='https://api.rosette.com/rest/v1/', sentence = "Default Sentence"):

    api = API(user_key=API_KEYS.ROSETTE_API_KEY, service_url=alt_url)
    params = DocumentParameters()
    label_set = set()
    final_response_list = []
    params["content"] = sentence
    params["language"] = "eng"
    # params["modelType"] = "dnn"
    try:
        response_dict = json.loads(json.dumps(api.sentiment(params)))["document"]
        response_list = []
        if str(response_dict["label"]) == "pos":
            response_list.append(["POSITIVE", float(response_dict["confidence"])])
        elif str(response_dict["label"]) == "neg":
            response_list.append(["NEGATIVE", float(response_dict["confidence"])])
        else:
            response_list.append(["NEUTRAL", float(response_dict["confidence"])])
        # ["sentiment"]
        # print response_dict
        return response_list[0]
    except RosetteException as exception:
        print(exception)


#
# RESULT = get_label(sentence=sentence)
# print(RESULT)
