# DataScience
This project is an activity for: **Universitat de Lleida -  Master's Degree in Informatics Engineering**<br>
Subject: **INTENSIVE DATA PROCESSING SYSTEMS**

## Preparing envirmoment (Mac/Linux)
- You need: Python 3 installed (no instructions hear for this)
- Install Virtualenv: ```pip install virtualenv```
- Create VirtualEnv: ```virtualenv venv```
- Activate: ```source venv/bin/activate```
> **_NOTE:_** For indications of VirtualEnv for other OS o more information: https://docs.python.org/3/library/venv.html

## Libraries to be installed
- Install Pandas library: ```pip install pandas```
- Install Seaborn libary: ```pip install seaborn```
- Install Numpy: ```pip install numpy```
- Install Jupyter: ```pip install jupyter```

## Where are all?
- {project}/notebooks/ : Jupiter Notebooks where are all tasks done.
- {project}/data/raw : where we have data to be processed
- {project}/data/processed : where clean data is saved

## Projects
### measures
#### preparing
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/measures.tgz to measures/data/raw
#### some notes
Data is in two formats csv and json.
We have data of 3 kind of sensor: Pressure, Temperature, Humidty
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

Data are analized with two orientations:
- **Analize all files of prices**: All files have the same format and the same type of data. 
For this we could make an only one notebook of Jupiter where each file can be selected and viwed. 
- **Analize one by one dataset files**: This files have a lot of columns an has a jupiter notebook for each one. 
It has analized column by column and try to get conclusions and clean and improve data.


### iris
#### preparing
data to download form:  http://codeandbeer.org/virtual/BigData/Datasets/iris.data to iris/data/raw
#### some notes
The file format is .data
This Dataset has five features which are Petal Length, Petal Width, Sepal Length, Sepal Width and Species Type.
The work has done to try to view some error and clean if any exists.

## How to create another project
- Install cookiecutter: ```pip install cookiecutter```
- Run this sentence and fill data that it ask for: ```cookiecutter https://github.com/drivendata/cookiecutter-data-science```

## Authors

* **Sergi Trujillo** - (https://github.com/sergitrujillo)
* **Jose Manuel Broto** - (https://github.com/josemanuel97)
* **Oriol Jorge** - (https://github.com/orioljorge)
