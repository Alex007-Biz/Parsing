import pprint
import requests

params = {
    'q': 'python'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
responce_json = response.json()
# pprint.pprint(responce_json)

print (f"кол-во репозиториев с Python: {responce_json['total_count']}")



