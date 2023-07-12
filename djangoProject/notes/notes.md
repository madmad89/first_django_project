a - windows / b - mac

1.create virtual environment
   a. python -m venv django_env
   b. python3 -m venv django_env

2.activate virtual environment
   a. django_env\Scripts\activate
   b. source django_env/bin/activate
   (For deactivate use only: deactivate)

3.check installed packages 
   pip list
   (The global pip list is pip3 list on mac)

4.install django framework
   pip install django

5.create django project
   django-admin startproject lista_cumparaturi

6.run django server (after cd lista_cumparaturi)
   python manage.py runserver

7.create application (after cd lista_cumparaturi)
   python manage.py startapp produse