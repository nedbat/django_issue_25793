This is what I did, reflected in the git history:

pip install -r requirements.pip
django-admin startproject djangomti
cd djangomti
python manage.py startapp mti
# ... edit mti/models.py ...
python manage.py makemigrations mti
# ... edit mti/models.py to remove the MTI model ...
python manage.py makemigrations mti
