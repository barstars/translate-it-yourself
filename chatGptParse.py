from g4f.client import Client
import g4f


class ParsGPT:

    def __init__(self):
        self.client = Client()

    def teach(self, text_user, orginal):
        try:
            text = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role":
                "user",
                "content":
                f'Оригинал цитаты:\n"{orginal}"\nМой перевод:\n"{text_user}"\nПожалуйста, проверьте мой перевод. Правильно ли я перевел? Если нет, укажите ошибки и предоставьте правильный перевод. Пожалуйста, объясните, как каждый элемент цитаты должен быть переведен и где я мог ошибиться.'
            }])
        except Exception as e:
            text = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":
                "user",
                "content":
                f'Оригинал цитаты:\n"{orginal}"\nМой перевод:\n"{text_user}"\nПожалуйста, проверьте мой перевод. Правильно ли я перевел? Если нет, укажите ошибки и предоставьте правильный перевод. Пожалуйста, объясните, как каждый элемент цитаты должен быть переведен и где я мог ошибиться.'
            }])
        finally:
            return text

    def translate(self, text_user):
        try:
            text = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{
                "role":
                "user",
                "content":
                f'я не знаю языки кроме Русского языка. Просто переведи на РУССКИЙ язык полностью и дай мне ничего больше не напиши.\n"{text_user}"'
            }])
        except Exception as e:
            text = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{
                "role":
                "user",
                "content":
                f'я не знаю языки кроме Русского языка. Просто переведи на РУССКИЙ язык полностью и дай мне ничего больше не напиши.\n"{text_user}"'
            }])
        finally:
            if (text[0] == text[-1]) and (text[-1] in ["'", '"']):
                text = text[1:-1]
            return text
        