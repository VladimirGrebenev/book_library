# Используйте базовый образ Python
FROM python:3.10

# Установите переменную окружения PYTHONUNBUFFERED в значение 1
ENV PYTHONUNBUFFERED=1

# Установите переменную окружения DJANGO_SETTINGS_MODULE в значение library_management.conf_prod
ENV DJANGO_SETTINGS_MODULE=library_management.conf_prod

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте файлы requirements.txt в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Скопируйте все файлы проекта в контейнер
COPY . .


# Запустите команду для миграции базы данных
RUN python manage.py collectstatic --noinput
COPY static /app/static


## Запустите команду для запуска сервера Django
#CMD ["gunicorn", "library_management.wsgi", "-b", "0.0.0.0:8080"]
