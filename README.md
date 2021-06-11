# Тестовое задание на вакансию Intern Backend-Developer в Aviasales

Приложение представляет из себя сервис, который на GET запрос возвращает из исходного .csv-файла информацию о полёте в JSON-формате.

## Дерево проекта
```
.
├── app
│   ├── Dockerfile
│   └── srcs
│       ├── app.py
│       ├── db.py
│       ├── flight_class.py
│       ├── flights.csv
│       ├── main.py
│       ├── requirements.txt
│       └── uwsgi.ini
├── docker-compose.yml
└── .env
```

## Установка и запуск

1. Склонировать репозиторий
```
git clone https://github.com/r-egorov/aviasales-intern
```

3. Поместить **.csv-файл** в директорию *./app/srcs*

2. Указать название **.csv**-файла в файле **.env** под переменной **CSV_FILE**.

3. Поднимаем сеть контейнеров с помощью docker-compose
```
docker-compose up -d
```
