# Базовый образ
FROM python:3.9-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY app.py .

# Запуск приложения
CMD ["python", "app.py"]
