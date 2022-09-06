#!/bin/sh


echo "**************** waiting for server volume ****************"
until cd /usr/src/app
do
    echo "**************** Waiting for server volume ****************"
done

echo "**************** migrating ****************"
python ./manage.py migrate --noinput --run-syncdb

echo "**************** running migrations ****************"
python ./manage.py makemigrations

python ./manage.py migrate --noinput --run-syncdb

echo "**************** collecting static ****************"
python ./manage.py collectstatic --noinput

echo "**************** starting gunicorn ****************"
gunicorn --bind 0.0.0.0:8004 git_track.wsgi --workers=2 --threads=4 --log-level debug --reload
echo "**************** gunicorn running ****************"