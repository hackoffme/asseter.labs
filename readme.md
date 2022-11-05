``` 
git clone https://github.com/hackoffme/asseter.labs.git . 
```


```
python -m venv env # activate source
pip install -r requirements.txt
python manage.py migrate
#load dataset
python manage.py load
python manage.py runserver

```
Импортировать в постман ```shop.postman_collection.json```
