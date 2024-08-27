from g4f.client import Client


client = Client()

def translate(text_for_translate):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f'Просто переведи на русский, не добавляй абсолютно ничего, только перевод и всё. Ничего больше не пиши.\n"{text_for_translate}"'}]
    )
    text = response.choices[0].message.content

    # if ( (text[0] in ["'", '"']) and (text[-1] in ["'", '"']) ):
    #         text = text[1:-1]

    return text