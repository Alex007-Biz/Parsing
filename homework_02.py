import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print(post)
else:
    print(f'Ошибка при получении данных. Код ответа: {response.status_code}')