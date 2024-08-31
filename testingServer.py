import requests


# url = "https://39423579-0f80-454b-97ad-4355b5debbd8-00-3cd1gsedchfma.sisko.replit.dev/translate"
# url = "http://127.0.0.1:80/translate"
url = "http://192.168.1.22:5000/get_random_quote"

response = requests.post(url,json={"tag":"busines"})
text = response.json()["quote"]
print(text)
print()
print("--------------------------")
print()

url = "http://192.168.1.22:5000/translate"
response = requests.post(url,json={"text":text})
tersnlate_text = response.json()["answer"]
print(tersnlate_text)