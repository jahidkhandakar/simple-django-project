# simple-django-project (Dockerized)

A simple Django app with search, signup/login, and country data display features—now Dockerized for easy setup and deployment!

### 🔧 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Setup & Run

### 1. Clone the Repository

git clone https://github.com/Manisha-Bayya/simple-django-project.git
cd simple-django-project

# bash: Start only the MySQL container to ensure the DB is ready:
docker-compose up -d db

# bash: load sample data
docker exec -i simple-django-mysql mysql -u root -proot world < world.sql

# bash: start the app
docker-compose up --build

# check this link
http://localhost:8000/



# Apply DB migrations
docker-compose exec web python manage.py migrate

# Rebuild search index
docker-compose exec web python manage.py rebuild_index

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access Django shell
docker-compose exec web python manage.py shell


# You can define the necessary environment variables directly in the docker-compose.yml file (inside the web service section), or you can create a .env file.

DB_NAME=world
DB_USER=root
DB_PASSWORD=root
DB_HOST=db
DB_PORT=3306
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
