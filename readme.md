
# Display Your Map on a Website Using Geopandas , Folium , Django , and Heroku

Side notes,  2022 - June

These notes provide a more detailed walkthrough to set up the app. 

Some special Requirements :

requirements are explained in the pdf document, here are a few additional explanations : 

You need admin rights only to install the Heroku Client. If you do not have them you can set up the app directly on the heroku portal.

After you may push your code through github. but you need to have  internet access and the site should not be blocked by company proxies.  

The tutorial of corey shafer is a must on the topic of Django. There is a vidéo on deploying the website to Heroku : "Python Django Tutorial: Full-Featured Web App". This tutorial is inspired from it.
https://coreyms.com/development/python/python-django-tutorials-full-series


Content : 
1- Data preparation example with Geopandas to prepare a Folium map
2- Serve our map locally in a Django application:
3- Deploy to Heroku


## 1- Data preparation example with Geopandas to prepare a Folium map

You may work on any python IDE like colab, vscode, pycharm, anaconda

- run the notebook or the script to produce an html file :
  - Install missing libraries (depending on your IDE)
  
- Note on geopandas installation:
Geopandas installation is straightforaward for Mac users , but for windows users it will require you to manually download and install the package and some on its dependencies. Fortunately there is a nice article that walks you through it: https://towardsdatascience.com/geopandas-installation-the-easy-way-for-windows-31a666b3610f

Once your libraries are set up the script will :
  - use geopandas to parse and process the data
  - folium is used to create the map
  - the map is saved in html format : "basel_map.html"

## 2- Serve our map locally in a Django application

### Prepare your developpement environment

- cd or create a folder like : cd ../02-Django_map
- create a virual env named "venv" : python3 -m venv venv (a common name for the target directory is .venv).
- activate environment : source venv/bin/activate
reference : https://docs.python.org/3/library/venv.html
- upgrate pip: pip install --upgrade pip
- install django : pip install django


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
  
- cd in the folder mysite/maps,
- create a template folder and a map folder in maps (its a naming convention in django) :  mkdir templates/maps
- copy the html file we created in part1 :  02-django_map/mysite/maps/templates/maps,
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
- make sure you are in the root of "mysite" folder
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


### specifics of Heroku in Django
- Our virtual environment comes in handy , we concentrate on libraries linked to our project

- in the root of mysite folder create a "procfile" to tell heroku how to run the application (to see the details look at Corey's video 21') : save the file with "web: gunicorn mysite.wsgi" inside, and procfile is named without any extension.
- You will need also to install gunicorn : "pip install gunicorn" . Gunicorn is a WSGI application server (it will invoke the wsgi.py file)
- Pip freeze and save your environment : pip freeze > requirements.txt
- add ".herokuapp.com" to ALLOWED_HOSTS in the mysite/mysite/settings.py file: 
ALLOWED_HOSTS = ["127.0.0.1" , ".herokuapp.com"]

### using the client

- create the app and specify your region : heroku create -a mybaselmap --region eu Note that the name must be unique
- Create an heroku config variable : heroku config:set DISABLE_COLLECTSTATIC=1 (you can set it up in the portal if no admin rights) Note : the topic of static files for is out of scope in this tutorial but you can follow along corey's video to set it up. Especially if you want to embed images in the map one day.
  
- push the code : git push heroku HEAD:master (if your proxy allows it).
- this part can a bit tricky and sometimes requires a bit of debugging
- debug: <https://stackoverflow.com/questions/26595874/heroku-src-refspec-master-does-not-match-any>  

- Note : its is easy to rename the app: heroku apps:rename newname but your need to follow the doc to update the git remote. see: 
- https://devcenter.heroku.com/articles/renaming-apps
You can aso create a new app but you also need to knwo how to manage your remotes

### Deploying with github

- create a repo on github 
- add origin to you local repo , see : https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories
- push you code in the repo 
- in the Heroku platform set up the automatic deploy : 
https://devcenter.heroku.com/articles/github-integration

- from now on everytime you push to master heroku will rebuild the website


Thats all, thanks & best 




