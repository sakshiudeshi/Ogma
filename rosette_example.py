# -*- coding: utf-8 -*-

"""
Example code to call Rosette API to get the category of a document (at a given URL).
"""
from __future__ import print_function

import argparse
import json
import os
import API_KEYS


from rosette.api import API, DocumentParameters, RosetteException

sentence = "an man on my cat shot Bob outside an pajamas outside Bob with my pajamas in my dog with my cat by an telescope"

def run(key, alt_url='https://api.rosette.com/rest/v1/', sentence = "Default Sentence"):
    """ Run the example """
    categories_url_data = "http://www.onlocationvacations.com/2015/03/05/the-new-ghostbusters-movie-begins-filming-in-boston-in-june/"
    url = categories_url_data
    # Create an API instance
    api = API(user_key=key, service_url=alt_url)
    params = DocumentParameters()

    # Use a URL to input data instead of a string
    params["content"] = sentence
    try:
        return api.categories(params)
    except RosetteException as exception:
        print(exception)


# PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
#                                  description='Calls the ' +
#                                  os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
# PARSER.add_argument('-k', '--key', help='Rosette API Key', required=True)
# PARSER.add_argument('-u', '--url', help="Alternative API URL",
#                     default='https://api.rosette.com/rest/v1/')

if __name__ == '__main__':
    # ARGS = PARSER.parse_args()
    RESULT = run(API_KEYS.ROSETTE_API_KEY, sentence=sentence)
    print(json.dumps(RESULT, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))
