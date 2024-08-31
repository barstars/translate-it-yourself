from g4f.client import Client
import g4f


class ParsGPT:

    def __init__(self):
        self.client = Client()

    def teach(self, text_user, orginal):
        print("Start GPT")
        text = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":
                "user",
                "content":
                f'Оргинал:\n"{orginal}"\nЭто мой перевод(перевод могут быт не быть):{text_user}\nСкажи правильно ли я переводил? Смысол я понял или нет? Где я ошибся? Какие правильное каие не правильное? Как можно ещё лучше? Как на самом деле оно переводится?'
            }])
        return text

    def translate(self, text_user):
        text = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{
                "role":
                "user",
                "content":
                f'я не знаю языки кроме Русского языка. Просто переведи на РУССКИЙ язык полностью и дай мне ничего больше не напиши.\n"{text_user}"'
            }])

        # Удаление кавычек, если они есть
        if (text[0] == text[-1]) and (text[-1] in ["'", '"']):
            text = text[1:-1]

        return text
