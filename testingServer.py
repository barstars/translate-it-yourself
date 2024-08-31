import requests


# url = "https://39423579-0f80-454b-97ad-4355b5debbd8-00-3cd1gsedchfma.sisko.replit.dev/translate"
# url = "http://127.0.0.1:80/translate"
ipadress = "http://192.168.1.22:5000"


url = ipadress+"/get_random_quote"
response = requests.post(url,json={"tag":"busines"})
orginal = response.json()["quote"]
print(orginal)
print()

user_translate = input("Попробуйте перевести и довести смысл этого цытаты по своему на руском языке: ")

url = ipadress+"/teach_me"
response = requests.post(url,json={"orginal":orginal,"user_translate":user_translate})
teach = response.json()["teach"]

print("--------------------------")
print()
print(teach)
input()