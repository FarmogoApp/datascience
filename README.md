# DataScience
This project is an activity for: **Universitat de Lleida -  Master's Degree in Informatics Engineering**<br>
Subject: **INTENSIVE DATA PROCESSING SYSTEMS**

## Preparing envirmoment (Mac/Linux)
- You need: Python 3 installed (no instructions hear for this)
- Install Virtualenv: ```pip install virtualenv```
- Create VirtualEnv: ```virtualenv venv```
- Activate: ```source venv/bin/activate```
- Install Pandas library: ```pip install pandas```
- Install Seaborn libary: ```pip install seaborn```

I used Pycharm IDE and all of this steps It has done and I could left someone.(say me, sorry)

## Where are all?
- {project}/notebooks/ : have Jupiter Notebooks where are all tasks done.
- {project}/data/raw : where are to download an extract data to process

##Projects
### measures
#### preparing
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/measures.tgz to measures/data/raw
#### some notes
Data is in two formats csv and json.
All files has same structure of information: time, value and sendor.
There are 3 types of notebooks: Analysing file by file, analisin files of same sensor and analising by same type of data.
- notebooks with name of data file analyses one value of sensor.
- notebooks starting by combine_data_{sensor}:   analises all data of same sensor.
- notebooks starting by combine_{type}_data: analises all sensors of same type of data.

### cryptocurrency
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/cryptocurrencypricehistory.tgz to cryptocurrency/data/raw 

### iris
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/iris.data to iris/data/raw

## How to create another project
- Install cookiecutter: ```pip install cookiecutter```
- Run this sentence and fill data that it ask for: ```cookiecutter https://github.com/drivendata/cookiecutter-data-science```