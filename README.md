# django-fusion
Deploy: https://fusion-mosp.herokuapp.com/
<br/>
Login
admin
password
admin

![Foo](https://raw.githubusercontent.com/matheusosp/django-fusion/main/Fusion.jpg)
<br/>
## Tests:<br/>
![Foo](https://raw.githubusercontent.com/matheusosp/django-fusion/main/fusion%20%E2%80%93%20test_views.py.jpg)

### TECHNOLOGIES
- Python
- Django (Web)
- django-adminlte2 (admin panel)
- django-stdimage (django images)
- model_mommy for tests
- gunicorn for deploy
- psycopg2-binary for postgress database with django
- dj-static for django static files
- dj-database-url for settings of deploy database with django
- textblob for translate project for any language

### To run locally

having python installed download the project and run the following commands

```
git clone git@github.com:matheusosp/django-fusion.git
cd django-fusion
git checkout main
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
