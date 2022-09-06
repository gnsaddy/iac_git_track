# docker/backend/Dockerfile
FROM python:3.10.4-slim
# set working directory
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/media

WORKDIR /usr/src/app

# prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# install mysql dependencies in python alpine image
RUN apt-get update -y
RUN apt-get gcc libc-dev mariadb-dev

RUN pip install --upgrade pip
RUN pip install gunicorn

ADD .. /usr/src/app
# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt
# install requirements
RUN python -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt
RUN pip freeze > requirements.txt

# copy entrypoint.sh
COPY ./entrypoint-local.sh .
RUN chmod +x ./entrypoint-local.sh

# run entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint-local.sh"]