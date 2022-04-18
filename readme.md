
# Display Your Map on a Website Using Geopandas , Folium , Django , and Heroku

Along this tutorial we will work mostly with the command line tool from a mac. Windows users will be able to follow though.
We will follow the official steps in the official documentations of the tools as much as possible.
On your computer you will need git and python >= 3.6. You will probably need admin rights on your company computer

The tutorial of corey shafer is a must on the topic : "Python Django Tutorial: Full-Featured Web App". This tutorial is inspired from it

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
- create a virual env named "venv" : python3 -m venv venv
- activate environment : source venv/bin/activate
- upgrate pip: pip install --upgrade pip
- install django : pip install django

### Follow "Writing your first Django app, part 1"

- go to the official documentation tutorial01:  <https://docs.djangoproject.com/en/4.0/intro/tutorial01/>
- the tutorial is about creating a "polls" app. We will just replace the name to a "maps" app
- so to be more relevant replace "polls" by "maps" everytime you see it
- copy paste every step to create the app and test a first webpage

### Skip "Writing your first Django app, part 2"

- part 2 about database, models and admin is out of scope for this tuturial
  
### Adapt "Writing your first Django app, part 3"

- in "Write views that actually do something";
- go to part "First, create a directory called templates in your polls directory. "
- Follow this part (Again "polls" is "maps")
- But instead of an "index.html" replace it with the map html file of part 1 :
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
  
### Setup git

- Follow : <https://www.youtube.com/watch?v=6DI_7Zja8Zc>

- install git if needed : <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- ititialize git : git init
- add a gitignore folder: touch .gitignore
- copy paste the pyhton gihub gitignore example
- add all files in the folder : git add -A
- check : git status : there should only be a dozen files there
- Commit for the fist time : git commit -m "Initial Commit"

### Setup Heroku

- install gunicorn : pip install gunicorn Gunicorn is a server
- create procfile
- sign up to heroku: <https://signup.heroku.com/login>
- install the Heroku cli : <https://devcenter.heroku.com/articles/heroku-cli>
- check that heroku is installed : heroku
- login : heroku login

## Push the code to Heroku to have a website ready with a map page

- pip freeze > requirements.txt  
- create the app (specify region) : heroku create -a mybaselmap --region eu
- add app to allowed hosts in settings.py
- disable collectstatic : heroku config:set DISABLE_COLLECTSTATIC=1
- push the code : git push heroku HEAD:master
- debug: <https://stackoverflow.com/questions/26595874/heroku-src-refspec-master-does-not-match-any>  
