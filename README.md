# addALanguageForMe
gpt-4

For start server:
gunicorn -w 4 --reload -b 0.0.0.0:8000 server:app
/get_random_quote - Даёт рандомную цитату - post запрос json {"tag":tag} - ответ json {"quote":quote}
/translate - Переводит - post запрос json {"text":text} - ответ json {"translate":translate}
/teach_me - Обесняет как правильно переводит и учит. Нужно англиский orginal и руский user_translate - post запрос json{"orginal":orginal,"user_translate":user_translate} - ответ json {"teach":teach}