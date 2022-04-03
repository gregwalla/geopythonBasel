
# Hello There

# along this tutorial we will work mostly with the command line tool under a mac OS 
# we will follow the official steps in the official documentations of the tools as much as possible
# on your computer you will need git and python >= 3.6
# you will probably need admin rights on your company computer

# the tutorial of corey shafer is a must on the topic : "Python Django Tutorial: Full-Featured Web App". This tutorial is greatly inspired from it

## We will start by a data preparation example with Geopandas to prepare a Folium map. 

### create a virtualenv in your folder (MAC) : 
- cd to folder : cd 01-data_preparation
- create virtual environment : python3 -m venv .
- activate environment : source bin/activate
- upgrate pip: pip install --upgrade pip
- install python libraries needed for this step : pip install -r requirements.txt
- run the notebook :
  - geopandas is used to parse the shapefile and process the data
  - folium is used to create the map
- deactivate environment : deactivate



## Then we will upload our map in a Django application. 
- cd to folder : cd ../02-Django_map
- create a virual env named "venv" : python3 -m venv venv 
- activate environment : source venv/bin/activate
- upgrate pip: pip install --upgrade pip
- install django : pip install django


# we will follow the official documentation to create the app and test a first webpage : 
go to  https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- check your django version : python -m django --version
- create a django project : django-admin startproject mysite
- create a new app : python manage.py startapp maps 
- cd to new app : cd mysite
- copy the map in the proper location : 
  - cd in the folder mysite/maps
  - create a template folder and a map folder in maps (its a naming convention in django) :  mkdir templates/maps
  - cd in the root folder cd ../../.. (europython)
  - copy the html file we created in part1 : cp 01-data_preparation/html/basel_kanton.html 02-django_map/mysite/maps/templates/maps

- modify the previousfiles so set it up the map to be rendered
go to  https://docs.djangoproject.com/en/3.2/intro/tutorial03/
scroll to the part : "Write views that actually do something" > "A shortcut: render()"
copy-paste the code in the maps/views file and adapt the application name

  - verify your Django project works : python manage.py runserver
- check the python manage.py startapp maps


# we will follow some stepts in a video to prepare the codebase : 

- Follow : https://www.youtube.com/watch?v=6DI_7Zja8Zc



- install git if needed : https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- ititialize git : git init 
- add a gitignore folder: touch .gitignore
- copy paste the pyhton gihub gitignore example
- add all files in the folder : git add -A
- check : git status : there should only be a dozen files there
- Commit for the fist time : git commit -m "Initial Commit"

- install gunicorn : pip install gunicorn Gunicorn is a server

- sign up to heroku: https://signup.heroku.com/login
- install the Heroku cli : https://devcenter.heroku.com/articles/heroku-cli
- check that heroku is installed : heroku
- login : heroku login

## Finally we will push the code to Heroku to have a website ready with a map page.

- set remote
- disable collectstatic
- 