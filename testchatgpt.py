from g4f.client import Client




client = Client()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Кто ты такой? какой модель? как тебе зовут? опиши себе полностю."}],
)
print("\n\n\n\n\n\n"+response.choices[0].message.content+"\n\n\n\n\n\n")