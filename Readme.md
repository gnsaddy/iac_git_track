docker-compose -f docker-compose.yml exec cms python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec cms python manage.py makemigrations


docker-compose -f docker-compose.yml exec cms python manage.py createsuperuser