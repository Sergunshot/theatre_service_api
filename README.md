# theatre_service_api

API service for theatre management written on DRF

## Installing using GitHub

Install PostgresSQL and create_db

 ```
 git clone https://github.com/Sergunshot/theatre_service_api
 cd theatre_api
 python -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
 set DB_HOST=<your db hostname>
 set DB_NAME=<your db name>
 set DB_USER=<your db username>
 set DB_PASSWORD=<your db password>
 set SECRET_KEY=<your Django secret key>
 set DEBUG=choose debug mode
 python manage.py migrate
 python manage.py loaddata dump.json
 python manage.py runserver
 ```

## Run with docker

Docker should be installed

```
docker-compose build
docker-compose up
```

## Getting access
 - create user via api/user/register/
 - get access token api/user/login/

## You can use admin credentials to test api
 - Email: `admin@admin.com`
 - Password: `admin`

## Features
 - Token authentication
 - Admin panel/admin
 - Documentation is located at api/schema/swagger-ui/
 - Managing orders and ticket
 - Creating plays with genres, actors
 - Creating theatre halls
 - Adding performances
 - Filtering play and performances