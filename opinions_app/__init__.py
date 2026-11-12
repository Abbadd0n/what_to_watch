from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config


# Загружаем переменные окружения из .env.
load_dotenv()

# Создаём Flask-приложение.
app = Flask(__name__)

# Загружаем настройки из корневого settings.py.
app.config.from_object(Config)

# Создаём базу данных.
db = SQLAlchemy(app)

# Подключаем Flask-Migrate.
migrate = Migrate(app, db)


# Импортируем модули в конце, чтобы избежать
# циклических импортов.
from opinions_app import models, views
from opinions_app import error_handlers, cli_commands
