FROM node:latest

RUN mkdir /app_frontend

WORKDIR /app_frontend

COPY package.json /app_frontend

RUN npm install

COPY . /app_frontend

EXPOSE 3000

CMD npm start