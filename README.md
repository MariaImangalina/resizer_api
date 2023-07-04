_Веб-сервис для загрузки и последующего уменьшения изображений на базе DRF и PostgreSQL_

## Запуск проекта

1. Клонировать репозиторий
```
git clone https://github.com/MariaImangalina/resizer_api.git
```
2. Запустить сборку контейнеров
```
docker-compose up
```

## Работа с проектом

URL http://localhost:8000/resize_picture/ принимает POST метод со следующими параметрами:
```
    :param file - оригинальный файл изображения
    :param width - ширина будущего измененного файла
    :param height - высота будущего измененного файла, опционально. В случае отсутствия высота будет расчитана из соотношения сторон оригинального изображения
```
В ответе будет получена ссылка на измененный файл. Пример ответа:
```
{
    "url": "http://localhost:8000/media/resized_images/d4db41dc09d80337f59ad1e9623befaa_555x10.PNG"
}
```

## Дополнительно:

1. Запустить тесты можно из контейнера бэка командой
```
docker exec -it resizer_api-backend-1 python manage.py test
```
2. На проекте настроено логгирование в журнал Django
```
docker logs resizer_api-backend-1
```