import requests


params = {
    'q': 'html'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()

print(response.status_code)
print(f"Количество репозиториев с html: {response_json['total_count']}")
