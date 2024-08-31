import requests


# url = "https://39423579-0f80-454b-97ad-4355b5debbd8-00-3cd1gsedchfma.sisko.replit.dev/translate"
# url = "http://127.0.0.1:80/translate"
# ipadress = "http://192.168.1.22:5000"
ipadress = "http://127.0.0.1:5000"
# while True:
	
random_quote_url = ipadress+"/get_random_quote"
response = requests.post(random_quote_url,json={"tag":"busines"})
orginal = response.json()["quote"]
print(orginal)
print()
print()

translate_url = ipadress+"/translate"
response = requests.post(translate_url,json={"text":orginal})
translate = response.json()["translate"]
print(translate)
print()
print()

# user_translate = input("Попробуйте перевести и довести смысл этого цытаты по своему на руском языке: ")
user_translate = "translate"

url = ipadress+"/teach_me"
response = requests.post(url,json={"orginal":orginal,"user_translate":user_translate})
teach = response.json()["teach"]

print("--------------------------")
print()
print(teach)
print()
print("+++++++++++++++++++++++++++++++++++++")
print()
print()
print()