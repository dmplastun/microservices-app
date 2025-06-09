# 🧪 Микросервисное приложение с Docker Compose

Этот проект демонстрирует базовую архитектуру микросервисного приложения, состоящего из двух сервисов на Flask, PostgreSQL в качестве БД и Nginx в роли reverse proxy. Также реализованы CI/CD через GitHub Actions и автоматическое развертывание на сервере.

---

## 🗺️ Архитектура проекта

- **service-a**: Простой Flask-сервис (микросервис)
- **service-b**: Второй Flask-сервис
- **db**: PostgreSQL 14
- **nginx**: Reverse proxy (маршрутизация запросов)
- **test**: Тестирование доступности сервисов
- **CI/CD**: GitHub Actions для сборки, тестирования и деплоя

---

## 📦 Структура папок
microservices-app/
── service-a/            # Первый микросервис
   ── app.py
   ── Dockerfile
── service-b/            # Второй микросервис
   ── app.py
   ── Dockerfile
── nginx/                # Nginx как reverse proxy
   ── Dockerfile
   ── nginx.conf
── test/                 # Автотесты
   ── test_app.py
   ── Dockerfile
── .env                  # Переменные окружения
── docker-compose.yml    # Описание контейнеров
── README.md             # Этот файл
── .github/
   ── workflows/
     ── ci-cd.yml  # CI/CD через GitHub Actions
---

## 🚀 Как запустить проект локально

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/ваш-username/microservices-app.git 
cd microservices-app
```
### 2. Установите зависимости: 

Убедитесь, что у вас установлены: 

    Docker  
    Docker Compose 
    
### 3. Запустите приложение:
```bash
docker compose up -d
```
### 4. Проверьте работу сервисов: 

    Service A: http://localhost/service-a 
    Service B: http://localhost/service-b 

### 🔍 Как проверить логи
```bash
docker compose logs
```
или
```bash
docker compose logs service-a
```
### 🧪 Как запустить тесты
```bash
docker compose run test
```
### 🛠️ Как пересобрать проект
Если вы внесли изменения в код: 
```bash
docker compose build --no-cache
docker compose up -d
```
### 🔄 Как остановить проект
```bash
docker compose down
docker compose down -v
```

### 🧳 CI/CD Pipeline
Проект поддерживает автоматическую сборку и развертывание через GitHub Actions. 
Функционал: 

    Сборка и публикация Docker-образов на Docker Hub
    Выполнение автотестов
    Развертывание на удаленном сервере через SSH
     
Требуется настройка: 

    Добавьте в Settings → Secrets and variables → Actions следующие секреты:
        DOCKER_HUB_USERNAME: ваш логин на Docker Hub
        DOCKER_HUB_TOKEN: токен из Docker Hub
        SERVER_HOST, SERVER_USER, SERVER_PASSWORD: параметры вашего сервера

### 🌐 Как развернуть на сервере
На удаленном сервере установите: 
    Docker
    Docker Compose
    
Подключитесь к серверу: 
```bash
ssh user@your-server-ip
``` 
 
Установите проект: 
```bash
git clone https://github.com/ваш-username/microservices-app.git 
cd microservices-app
docker compose up -d
``` 
👤 Автор 

Ваше имя
📧 dmitrij.plastun@gmail.com (необязательно)
🔗 https://github.com/dmplastun
🙌 Спасибо за использование! 

Если понравилось — ставьте звезду ⭐ и делитесь с коллегами! 
