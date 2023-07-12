# notes for MacOS

# create virtual environment
mkdir .venv
pip3 install pipenv
pipenv install
pipenv shell
touch misc.py
pipenv --where

# install django
pipenv install django

# create new django project and run
django-admin startproject prim
cd prim
python manage.py runserver

# create new subapp inside our app
python manage.py startapp doi


pipenv install django

django-admin startproject prim 
(prim e numele proiectului, puteti pune orice nume)

python manage.py runserver
- comanda pentru a rula serverul pe localhost
http://127.0.0.1:8000/
- aceasta e pagina de localhost, adica pagina unde se va rula proiectul nostru
- acesta e adresa care ruleaza pe calculatorul nostru 
- 127.0.0.1 putem scrie localhost
- 8000 e portul pe care ruleaza serverul

CTRL+C - opreste serverul

Creez un folder gol in explorer, right-click-> open in vscode

mkdir .venv
-mkdir creeaza un folder
.venv - virtual environment, va stoca toate fisierele tehnice

ni misc.py - creeaza un fisier cu ni= new item

pip install pipenv - instaleaza pipenv

pipenv install --python 3.11 - creeaza un virtual environment cu python 3.11
--python 3.11 - este optional daca vrem sa specificam versiunea de python

pipenv shell - activeaza virtual environment

pipenv install django
- instaleaza django in virtual environment
- va aparea in pipfile la [packages]
django = "*" = * inseamna ultima versiunea

<django-admin startproject prim>
- am creat un proiect django numit prim

Dupa care in terminal <cd prim> ca sa intram in folderul proiectului

Pentru a rula serverul:
<python manage.py runserver>
Se va deschide la adresa http://127.0.0.1:8000/
- adica localhost la portul default 8000
- echivalent cu http://localhost:8000/

Pentru a opri serverul:
CTRL+C in terminal

Instructiuni pentru instalarea environment cu pipenv (edited) 

Vom folosi comenzi de terminal (Terminal- New Terminal) pentru a ne seta manual un mediu de codare/ virtual environment
In PyCharm acesta se creeaza automat 

Creati un folder separat si apoi open with VSCode (click dreapta pe folder)
pip install pipenv
mkdir .venv creeaza un folder venv unde vor fi stocate fisierele tehnice
ni misc.py creeaza un fisier python 

pipenv install
pipenv shell (edited) 

In dreapta jos trebuie sa apara ceva de genu 3.10.1 (venv: pipenv) 
Acesta trebuie sa fie executorul local de python.
Eventual aveti nevoie sa instalati python din extensii (in stanga e un buton cu 4 patrate, unu iese afara)

1. In doi/views.py mi-am creat o functie care imi 
returneaza o pagina web
2. In prim/urls.py am creat o cale catre functia din views.py
Important: trebuie sa importam functia din views.py in urls.py
from doi.views import salut

In terminal am rulat 
python manage.py runserver
Pentru a porni serverul pe localhost (default port 8080)

http://localhost:8000/wazup
==
http://127.0.0.1:8000/wazup

CTRL+C pentru a opri serverul in terminal