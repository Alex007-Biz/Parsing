import pprint
import requests

params = {
    'q': 'python'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()
# pprint.pprint(responce_json)

print (f"кол-во репозиториев с Python: {response_json['total_count']}")



