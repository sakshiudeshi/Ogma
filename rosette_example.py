import json

import API_KEYS


from rosette.api import API, DocumentParameters, RosetteException

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"

def run(alt_url='https://api.rosette.com/rest/v1/', sentence = "Default Sentence"):

    api = API(user_key=API_KEYS.ROSETTE_API_KEY, service_url=alt_url)
    params = DocumentParameters()

    params["content"] = sentence
    try:
        return api.categories(params)
    except RosetteException as exception:
        print(exception)


if __name__ == '__main__':
    # ARGS = PARSER.parse_args()
    RESULT = run(sentence=sentence)
    print(json.dumps(RESULT, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))
