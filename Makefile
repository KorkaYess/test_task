all:
	docker-compose build

start:
	docker-compose up

daemon:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

shell:
	docker-compose run web /bin/sh

migrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate
