# Django_DRF_React quick starter

### Functionality
* [x] Basic Signup & Login/Logout with JWT (no Redux, no Reset password)
* [x] API documentation with DRF Swagger
* [x] local/dev/prod settings for Django backend 

## Retrieve code
```
$ git clone https://github.com/IvanPrytula/inoxoft-task1.git
$ cd inoxoft-task1
```


## Installation
Accordingly to your OS/Architecture follow instructions on official sites. 
* Install [Docker](https://hub.docker.com/search/?type=edition&offering=community) 
* Install [Docker Compose](https://docs.docker.com/compose/install/)

##### Without Docker because:
* `$ docker-compose build` <-- works
* `$ docker-compose up`    <-- doesn't work ((

##### Alternative Steps to Try How Application works:
```
$ cd backend
$ pip3 install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver
```

```
$ cd frontend
$ npm install
$ npm start
```
