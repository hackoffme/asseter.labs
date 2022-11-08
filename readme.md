```
git clone https://github.com/hackoffme/asseter.labs.git . 
docker-compose up --build
#load dataset
docker-compose exec web bash
python manage.py load
```
Импортировать в постман ```shop.postman_collection.json```
flower http://127.0.0.1:5555/
