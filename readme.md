
# Display Your Map on a Website Using Geopandas , Folium , Django , and Heroku



Along this tutorial we will work mostly with the command line tool from a mac.
We will emphasize on following the official documentations of the tools.

Thus : 1-Windows instruction will also usually present in the documentations and
       2-these documentations are maintained.

Main Requirements : 
On your computer you will need a python > 3.6 installation at the time of this tutorial (june 22).
You need admin rights to install the Heroku Client. If you do not have them you will need to set up the app directly on the heroku portal. After you may push your code through github.
You will also need git that is used to push the code to Heroku.

The tutorial of corey shafer is a must on the topic of Django. There is a vidéo on deploying the website to Heroku : "Python Django Tutorial: Full-Featured Web App". This tutorial is inspired from it.

Agenda : 
1- We start by a data preparation example with Geopandas to prepare a Folium map
2- Serve our map locally in a Django application:
  Prepare your developpement environment
  Follow django official tutorial "Writing your first Django app, part 1"
  Skip "Writing your first Django app, part 2"
  Adapt "Writing your first Django app, part 3"
3- Deploy to Heroku


## 1- We will start by a data preparation example with Geopandas to prepare a Folium map

You may work on any python IDE, colab, vscode, pycharm, anaconda ...  

Create a virtualenv in your folder (MAC) :
reference : https://docs.python.org/3/library/venv.html

- create and cd to a folder like : cd 01-data_preparation
- check your python3 version : which pyhton3
- if above 3.7 continue , else it is advised to get a later version of python
- create virtual environment : python3 -m venv venv
- activate environment : source venv/bin/activate (if in root folder)
- you may want to upgrage pip: pip install --upgrade pip

Create a virtualenv in your folder (Windows) :

- run the notebook or the script :
  - Install missing libraries (depending on your IDE)
  
- Note on geopandas installation:
Geopandas installation is straightforaward for Mac users , but for windows users it will require you to manually download and install the package and some on its dependencies. Fortunately there is a nice article that walks you through it: https://towardsdatascience.com/geopandas-installation-the-easy-way-for-windows-31a666b3610f

Once your libraries set up :
  - geopandas is used to parse the shapefile and process the data
  - folium is used to create the map
  - A map is saved in html format : "basel_map.html"
  - deactivate environment : deactivate

## 2- Serve our map locally in a Django application

### Prepare your developpement environment

- cd or create a folder licke : cd ../02-Django_map
- create a virual env named "venv" : python3 -m venv venv (a common name for the target directory is .venv).
- Note : there is one environment for data prep and one for our web app. They are intentionnaly kept separate. 
- activate environment : source venv/bin/activate
- upgrate pip: pip install --upgrade pip
- install django : pip install django
reference : https://docs.python.org/3/library/venv.html

### Follow django official tutorial "Writing your first Django app, part 1"

- go to the official documentation tutorial01:  <https://docs.djangoproject.com/en/4.0/intro/tutorial01/>
- the tutorial is about creating a "polls" app. 
- Part 1 of the tutorial is about creating a project and launching a "Hello world" polls app
- We will just replace the word "polls" to a "maps" all the way

- copy paste every step of part 1 to create the app and test a first hello world webpage

### Skip "Writing your first Django app, part 2"

- part 2 is about database, models and admin. It is out of scope for this tuturial which focuses on deployment. 
  
### Adapt "Writing your first Django app, part 3"

- part 3 introduces the "view" of the model-view-template (MVT):
- "A view is a “type” of web page in your Django application that generally serves a specific function and has a specific template"
  
- in pat 3 - section "Write views that actually do something";
- go to part "First, create a directory called templates in your polls directory. "
- Follow this part (Again "polls" is to be replaced "maps")
- But instead of an "index.html" file replace it with the basel_map.html file of part 1 :
  
     cd in the folder mysite/maps,
     create a template folder and a map folder in maps (its a naming convention in django) :  mkdir templates/maps
     cd in the root folder cd ../../..,
     copy the html file we created in part1 : cp 01-data_preparation/html/basel_kanton.html 02-django_map/mysite/maps/templates/maps,
- scroll to the part : "Write views that actually do something" > "A shortcut: render()"
copy-paste the code in the maps/views file
- delete second (from .models ..), 4th (latest_questi ..) and 5th (context = ..) lines
- adapt the application name (Again "polls" is "maps")
- cd in the folder mysite/maps
- you can check your Django project works : python manage.py runserver
- navigate to : http://127.0.0.1:8000/maps

## 3- Deploy to Heroku
  
Deployment to Heroku is done though git. 

### Setup git

- Corey Shafer Video on the topic : <https://www.youtube.com/watch?v=6DI_7Zja8Zc>

- install git if needed : <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- ititialize a git repo : git init
- add a gitignore folder: touch .gitignore
- or copy paste the pyhton gihub gitignore template (mainly to ignore .venv): 
- https://github.com/github/gitignore/blob/main/Python.gitignore
- add all files in the folder : git add -A
- check : git status : there should only be a dozen files there
- Commit for the fist time : git commit -m "Initial Commit"

## Setup Heroku

- sign up to heroku: <https://signup.heroku.com/login>
- if you have admin rights - install the Heroku cli : <https://devcenter.heroku.com/articles/heroku-cli>
- Note : if you do not you will be able to manually perform some of the steps from the heroku portal
- check that heroku is installed : heroku
- login : heroku login

## Push the code to Heroku 

- Our virtual environment comes in handy , we concentrate on libraries linked to our project
- cmd: pip freeze > requirements.txt  
- create the app and specify your region : heroku create -a mybaselmap --region eu (you can set it up in the portal if no admin rights)
- Note that the name must be unique
- in the root of mysite folder create a "procfile" to tell heroku how to run the application (to see the details look at Corey's video 21') : save the file with "web: gunicorn mysite.wsgi" inside, and without any extension.
- You will need also to install gunicorn : "pip install gunicorn" . Gunicorn is a WSGI application server (it will invoke the wsgi.py file)
- Create an heroku config variable : heroku config:set DISABLE_COLLECTSTATIC=1 (you can set it up in the portal if no admin rights) Note : the topic of static files for is out of scope in this tutorial but you can follow along corey's video to set it up. Especially if you want to embed images in the map one day.  
- add ".herokuapp.com" to ALLOWED_HOSTS in the mysite/mysite/settings.py file: 
ALLOWED_HOSTS = ["127.0.0.1" , ".herokuapp.com"]
- push the code : git push heroku HEAD:master (if your proxy allows it).
- this part can a bit tricky and sometimes requires a bit of debugging
- debug: <https://stackoverflow.com/questions/26595874/heroku-src-refspec-master-does-not-match-any>  

- Note : its is easy to rename the app: heroku apps:rename newname

-Deploying with github :  
  - create a repo on github 
  - add origin to you local repo 
  - push you code in the repo 
  - in the Heroku platform set up the automatic deploy : 
  https://devcenter.heroku.com/articles/github-integration
  - from now on everytime you push to master heroku will rebuild the website

Thats all, thanks & best 




