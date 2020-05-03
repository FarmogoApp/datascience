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
- Install Numpy: ```pip install numpy```
- Install Jupyter: ```pip install jupyter```

We have used Pycharm IDE and all of this steps It has done and I could left someone.(say me, sorry)

## Where are all?
- {project}/notebooks/ : Jupiter Notebooks where are all tasks done.
- {project}/data/raw : where we have data to be processed
- {project}/data/processed : where clean data is saved

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
We have included Util.py with load and save functions

### cryptocurrency
#### preparing
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/cryptocurrencypricehistory.tgz to cryptocurrency/data/raw 
#### some notes
All files are in csv format


### iris
#### preparing
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/iris.data to iris/data/raw
#### some notes
The file format is .data
This Dataset has five features which are Petal Length, Petal Width, Sepal Length, Sepal Width and Species Type.

## How to create another project
- Install cookiecutter: ```pip install cookiecutter```
- Run this sentence and fill data that it ask for: ```cookiecutter https://github.com/drivendata/cookiecutter-data-science```

## Authors

* **Sergi Trujillo** - (https://github.com/sergitrujillo)
* **Jose Manuel Broto** - (https://github.com/josemanuel97)
* **Oriol Jorge** - (https://github.com/orioljorge)
