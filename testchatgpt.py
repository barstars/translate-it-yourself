from g4f.client import Client
import g4f

client = Client()
response = client.chat.completions.create(
    model="gpt-4-turbo",
    provider=g4f.Provider.Bing,
    messages=[{"role": "user", "content": "Какой у тебя модель?"}],
)
print(response.choices[0].message.content)