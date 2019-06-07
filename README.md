### Prerequisites
1- start documenting for virtualenv and install it  pip install virtualenv
  then activate it from scripts/bin/activate

2- install all flask and flask-restful and gunicorn
**Gunicorn is a WSGI HTTP server that will handle requests made to your app when it is deployed. It is what most folks use to deploy python apps.

3- install heroku cli from their website

### Config

4- create a ```` procfile : web: gunicorn -w 4 my_app_name:app why? my_app_name is my_app_name.py and and app is flask name in my_app_name ````

5- create a req txt by ```` pip freeze > requirements.txt ````

6- create a runtime.txt that conatins: python-3.7.2

7- copy/paste a hello world code.

8- create a .gitignore containes 
---
env

*.pyc

---

9-git init, git add , git commit


10- heroku login

12- heroku create yourapp

11- git push heroku master 


*error ? so heroku git:remote -a yourapp *switch? : remote add origin https://github.com/AbdelghaniAnnani/flask-example


13- run: heroku open

12- logs: heroku logs --tail


### pdb not works? try this


breakpoint : import pdb; pdb.set_trace()

app.run(debug=True)

### url params try this?

@app.route('/lang/<int:id>', methods=['GET'])

@app.route('/lang/<string:id>', methods=['GET'])






