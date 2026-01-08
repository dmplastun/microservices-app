# 🧪 Microservices App with Docker Compose

This project demonstrates a basic microservices architecture consisting of two Flask services, PostgreSQL as the database, and Nginx as a reverse proxy. It also includes CI/CD via GitHub Actions and automatic deployment to a server.

---

## 🗺️ Project Architecture

-**service-a**: Simple Flask service (microservice)

-**service-b**: Second Flask service

-**db**: PostgreSQL 14

-**nginx**: Reverse proxy (request routing)

-**test**: Service availability testing 

-**CI/CD**: GitHub Actions for building, testing, and deployment 

---

## 📦 Folder Structure
```
microservices-app/
├── service-a/            # First microservice
│   ├── app.py
│   └── Dockerfile
├── service-b/            # Second microservice
│   ├── app.py
│   └── Dockerfile
├── nginx/                # Nginx as reverse proxy
│   ├── Dockerfile
│   └── nginx.conf
├── test/                 # Automated tests
│   ├── test_app.py
│   └── Dockerfile
├── .env                  # Environment variables
├── docker-compose.yml    # Container definitions
├── README.md             # This file
└── .github/workflows/ci-cd.yml  # CI/CD via GitHub Actions
```
---

## 🚀 How to Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/microservices-app.git 
cd microservices-app

```
### 2. Install dependencies: 

Убедитесь, что у вас установлены: 
```
Docker  
Docker Compose 
```
    
### 3. Start the application:
```
docker compose up -d
```
### 4. Check the services:
```
Service A: http://localhost/service-a 
Service B: http://localhost/service-b 
```

### 🔍 How to check logs
```
docker compose logs
```
or
```
docker compose logs service-a
```
### 🧪 How to run tests
```
docker compose run test
```
### 🛠️ How to rebuild the project
If you made changes to the code:
```
docker compose build --no-cache
docker compose up -d
```
### 🔄 How to stop the project
```
docker compose down
docker compose down -v
```

### 🧳 CI/CD Pipeline
The project supports automatic building and deployment via GitHub Actions.
Features:
```
Building and publishing Docker images to Docker Hub
Running automated tests
Deploying to a remote server via SSH
```

Required setup:
```
Add the following secrets in Settings → Secrets and variables → Actions:
    DOCKER_HUB_USERNAME: your Docker Hub login
    DOCKER_HUB_TOKEN: token from Docker Hub
    SERVER_HOST, SERVER_USER, SERVER_PASSWORD: your server parameters
```

🌐 How to Deploy to a Server
On the remote server, install:
```
Docker
Docker Compose
```    
Connect to the server:
```
ssh user@your-server-ip
``` 
 
Install the project:
```
git clone https://github.com/your-username/microservices-app.git 
cd microservices-app
docker compose up -d

``` 
👤 Author

📧 dmitrij.plastun@gmail.com

🔗 https://github.com/dmplastun

🙌 Thanks for using it!

If you liked it — give it a star ⭐ and share with colleagues!
