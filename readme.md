
# Display Your Map on a Website Using Geopandas , Folium , Django , and Heroku

Speak more about the scope 
skip details off polls app 
explain advantages & inconvenients of tools 
just serve the html
explain tools 
tel that docs will be shared 
start with the output
explain the benefits (modify easily , search for an integrated web app, best practies , repeat .. )
code a bit 


Along this tutorial we will work mostly with the command line tool from a mac.
We will emphasize on following the official documentations of the tools.

Thus : 1-Windows instruction will also usually present in the documentations and
       2-these documentations are maintained.

On your computer you will need a python >= 3.6 installation at the time of this tutorial.
You need admin (sudo) rights (if your are on your company's computer).
You will also need git that is used to push the code to Heroku.

The tutorial of corey shafer is a must on the topic : "Python Django Tutorial: Full-Featured Web App". This tutorial is inspired from it.

Agenda : 
1- We will start by a data preparation example with Geopandas to prepare a Folium map
  Create a virtualenv in your folder (MAC)
  Create a virtualenv in your folder (Windows)
2- Serve our map locally in a Django application:
  Prepare your developpement environment
  Follow django official tutorial "Writing your first Django app, part 1"
  Skip "Writing your first Django app, part 2"
  Adapt "Writing your first Django app, part 3"


## 1- We will start by a data preparation example with Geopandas to prepare a Folium map

Create a virtualenv in your folder (MAC) :

- cd to folder : cd 01-data_preparation
- check your python3 version : which pyhton3
- if above 3.7 continue , else it is advised to get a later version of python
- create virtual environment : python3 -m venv venv
- activate environment : source bin/activate (if in root folder)
- upgrate pip: pip install --upgrade pip
- install python libraries needed for this step : pip install -r requirements.txt
- run the notebook or the script :
  - geopandas is used to parse the shapefile and process the data
  - folium is used to create the map
- A map is saved in html format
- deactivate environment : deactivate

## 2- Serve our map locally in a Django application

### Prepare your developpement environment

- cd to folder : cd ../02-Django_map
- create a virual env named "venv" : python3 -m venv venv (a common name for the target directory is .venv).
- activate environment : source venv/bin/activate
- upgrate pip: pip install --upgrade pip
- install django : pip install django
reference : https://docs.python.org/3/library/venv.html

### Follow django official tutorial "Writing your first Django app, part 1"

- go to the official documentation tutorial01:  <https://docs.djangoproject.com/en/4.0/intro/tutorial01/>
- the tutorial is about creating a "polls" app. 
- Part 1 is about creating a project and launching a "Hello world" polls app
- We will just replace the name to "polls" to a "maps" all the way along
- so replace "polls" by "maps" everytime you see it and follow along
- copy paste every step of part 1 to create the app and test a first hello world webpage

### Skip "Writing your first Django app, part 2"

- part 2 is about database, models and admin. It is out of scope for this tuturial that focuses on deployment.
  
### Adapt "Writing your first Django app, part 3"

- part 3 introduces the "view" of the model view template:
- "A view is a “type” of web page in your Django application that generally serves a specific function and has a specific template"
  
- in section "Write views that actually do something";
- go to part "First, create a directory called templates in your polls directory. "
- Follow this part (Again "polls" is to be replaced "maps")
- But instead of an "index.html" file replace it with the basel_map.html file of part 1 :
- 
     cd in the folder mysite/maps,
     create a template folder and a map folder in maps (its a naming convention in django) :  mkdir templates/maps
     cd in the root folder cd ../../..,
     copy the html file we created in part1 : cp 01-data_preparation/html/basel_kanton.html 02-django_map/mysite/maps/templates/maps,
- scroll to the part : "Write views that actually do something" > "A shortcut: render()"
copy-paste the code in the maps/views file
- delete second (from .models ..), 4th (latest_questi ..) and 5th (context = ..) lines
- adapt the application name (Again "polls" is "maps")
- cd in the folder mysite/maps
- verify your Django project works : python manage.py runserver
- to confirm : in Settings add your app  
- navigate to : http://127.0.0.1:8000/maps

## 3- Deploy to Heroku
  
### Setup git

- Follow : <https://www.youtube.com/watch?v=6DI_7Zja8Zc>

- install git if needed : <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- ititialize git : git init
- add a gitignore folder: touch .gitignore
- or copy paste the pyhton gihub gitignore template (mainly to ignore .venv): 
- https://github.com/github/gitignore/blob/main/Python.gitignore
- add all files in the folder : git add -A
- check : git status : there should only be a dozen files there
- Commit for the fist time : git commit -m "Initial Commit"

## Setup Heroku

- sign up to heroku: <https://signup.heroku.com/login>
- install the Heroku cli : <https://devcenter.heroku.com/articles/heroku-cli>
- Note : the heroku client requires admin rigths 
- check that heroku is installed : heroku
- login : heroku login

## Push the code to Heroku to have a website ready with a map page

- this is where our virtual environment comes in handy , we concentrate on libraries linked to our project
- cmd: pip freeze > requirements.txt  
- create the app and specify your region : heroku create -a mybaselmap --region eu
- Note that the name must be unique
- create a procfile to tell heroku how to run the application (Corey's video 21') : web: gunicorn mysite.wsgi
- install gunicorn : pip install gunicorn. Gunicorn is a WSGI application server
  (it will invoke the wsgi.py file)
- Create an heroku config variable : heroku config:set DISABLE_COLLECTSTATIC=1
- (the topic of static files for is out of scope in this tutorial but you can follow along corey's video to set it up)
- add the app name to ALLOWED_HOSTS in mysite/mysite/settings.py file: 
- ALLOWED_HOSTS = ["127.0.0.1" , ".herokuapp.com"]
- push the code : git push heroku HEAD:master
- this part is a bit tricky and sometimes requires a bit of debugging
- debug: <https://stackoverflow.com/questions/26595874/heroku-src-refspec-master-does-not-match-any>  

-rename the app:
heroku apps:rename newname
-deploying with github :  currently out of order due to a security issue
