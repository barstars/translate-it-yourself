from g4f.client import Client
import g4f


class ParsGPT:

    def __init__(self):
        self.client = Client()

    def teach(self, text_user, orginal):
        text = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role":
                "user",
                "content":
                f'Оригинал цитаты:\n"{orginal}"\nМой перевод:\n"{text_user}"\nПожалуйста, проверьте мой перевод. Правильно ли я перевел? Если нет, укажите ошибки и предоставьте правильный перевод. Пожалуйста, объясните, как каждый элемент цитаты должен быть переведен и где я мог ошибиться.'
            }])
        return text

    def translate(self, text_user):
        text = g4f.ChatCompletion.create(
            model='gpt-4',
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
