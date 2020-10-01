# mrent
Projeto - Práticas profissionais em análise e desenvolvimento de sistemas

## Building
1 - Configure uma virtual env python 3.6.x
```bash
$ python -m venv venv
```
2 - Ative e instale os project requirements
```bash
$ source venv/Scrits/activate.bat
$ pip install -r requirements.txt
```
3 - navegue até a pasta principal do projeto onde está o arquivo manage.py e run
```bash
$ python manage.py runserver
Então visit http://localhost:8000 para ver o app.
```

## Deploy to Heroku

Run os comandos abaixo para o deploy no Heroku:

```bash
$ heroku login
$ git init
$ heroku git:remote -a mrent1
$ git add .
$ git commit -m "any comment"
$ git push heroku master
```
