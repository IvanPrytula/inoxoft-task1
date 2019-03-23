FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /app_backend

WORKDIR /app_backend

COPY requirements.txt /app_backend

RUN pip install -r requirements.txt

COPY . /app_backend

EXPOSE 8000

CMD python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000