import requests

img = "https://www.plitkanadom.ru/upload/iblock/57f/Equipe-Art-Nouveau-1.jpg"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
