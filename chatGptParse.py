from g4f.client import Client
import g4f


class ParsGPT:
    client = Client()

    def translateClient(self, text_user):
        print("Start gpt")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":
                "user",
                "content":
                f'Просто переведи на русский язык.\n"{text_user}"'
            }])
        text = response.choices[0].message.content

        return text

    def translate(self, text_user):
        text = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{
                "role":
                "user",
                "content":
                f'Просто переведи на РУССКИЙ язык и дай мне ничего больше не напиши.\n"{text_user}"'
            }])

        if ((text[0] in ["'", '"']) and (text[-1] in ["'", '"'])):
            text = text[1:-1]

        return text
