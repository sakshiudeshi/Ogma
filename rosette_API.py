from rosette.api import API
import API_KEYS


api = API(user_key=API_KEYS.ROSETTE_API_KEY)
result = api.ping()
print("/ping: ", result)
