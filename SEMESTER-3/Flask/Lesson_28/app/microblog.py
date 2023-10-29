from app import app

# Прежде чем приступить к созданию блога на Flask, убедитесь, что в вашей системе установлен Python и pip. Затем выполните следующие шаги:

# 1. Создайте новую директорию microblog:

# mkdir microblog
# cd microblog


# 2. Создайте виртуальную среду внутри директории microblog:

# python -m venv venv


# 3. Активируйте виртуальную среду:

# Windows:
# venv\Scripts\activate


# Linux/macOS:
# source venv/bin/activate


# 4. Установите необходимые модули Flask, python-dotenv и Flask-WTF:

# pip install flask python-dotenv flask-wtf


# 5. В директории microblog создайте следующую структуру файлов и папок:

# microblog/
#   venv/
#   app/
#     __init__.py
#     routes.py
#   microblog.py
#   .env


# 6. Расположите следующий код внутри файла microblog.py:

# from app import app


# 7. Создайте файл .env и добавьте в него следующее:

# FLASK_APP=microblog.py


# Теперь ваша структура файлов и папок должна выглядеть так:

# microblog/
#   venv/
#   app/
#     __init__.py
#     routes.py
#   microblog.py
#   .env
