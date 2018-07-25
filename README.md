# Wiki Farm

## Description

#### The app allows the user to:
1. Click anywhere on the map,
2. Get the x,y coordinated.
3. Perform a Query on the coordinate selected.
4. There are three data sources,
- Dark Sky - Gives current weather conditions.
- Crop Database - A collection of research about some selected Crops e/g Maize, Coffee, Tea among others.
- Soil Database e.g Ph, soil temp, moisture contents and other data about kenya soil.

5. Allow the farmer to check the current climatic conditions near him/her , check aganaist the crop database to predict the likely
best crop the farmer can plant.

 + Created on, July 10th 2018

## Technologies used
+ Django
+ Geodjango
+ Angular material
+ Jquery
+ Leafletjs
+ HTML5
+ Css3
+ Postgresql
+ Postgis
+ Git

## Development and Setup.
### prerequisites
- Python 3.6 should be installed
- django 1.11
- install other packages provided in the requirements.txt file
- Running the application.
- Visit this link to view on any browser.

### Installation.
- Ensure python3.6 is installed.
- Clone the repository git clone <repo url>
- create a virtual environment virtualenv <envname> and activate source <envname>/bin/activate
- Install the required packages pip3 install -r requirements.txt
- Create a postgresql database.
- open the psql terminal by typing psql -h localhost -U <username>
- Once on the psql terminal create the database ```CREATE DATABASE ``
- Create postgis extension ```CREATE EXTENSION postgis``` and ```CREATE EXTENSION postgis-topology```
- Quit the shell \q
- Once the database is setup, make migrations, this creates database schemas for the application python manage.py -makemigrations
- Then create the actual database tables by python manage.py migrate
- Start the application by python manage.py runserver and open http://127.0.0.1:8000 in the browser.
  
## Test Driven Development
Testing was done using python inbuild test tool called unittest to test database and form models.

## Reccomendations
1. Given data on the soil property, and the climate, can you advise what ferilizer to use.
2. Work on Angular UI.
3. Quality of data.

## Further help
To get Further help you can visit the official python and django documentation.

## Licence
MIT (c) 2018 muriithi derrick
