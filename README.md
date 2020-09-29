# mrent
Projeto - Práticas profissionais em análise e desenvolvimento de sistemas

## Building
1 - configure uma virtual env python 3.6.x

```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
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
