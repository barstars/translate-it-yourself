import requests


# url = "https://2a655484-5187-4b30-be4d-345e15acb58b-00-s9p3l077pyvy.sisko.replit.dev/translate"
url = "http://127.0.0.1:80/translate"

response = requests.post(url,json={"tag":"smile"})
print(response.json()["answer"])