import pprint
import requests

response = requests.get('https://otdelkino.ru/')
print(response.status_code)
if response.ok:
    print("Запрос успешно выполнен")
else:
    print("Ошибка")
# print(response.content)

response_json = response.json()
pprint.pprint(response_json)
