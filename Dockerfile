# Используем Python 3.11
FROM python:3.11-slim

# Создаем рабочую директорию
WORKDIR /app

# Копируем все файлы в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir python-telegram-bot requests

# Команда запуска бота
CMD ["python", "bot.py"]
