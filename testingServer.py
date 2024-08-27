import requests

url = "https://muhammedeveloper1.pythonanywhere.com/translate"

response = requests.post(url,json={"tag":"af"})
print(response.text)