# All file have the same structure we can load with same program
import json
import pandas as pd
import sys


def loadJson(file, valueColName='value', nrows=-1, path="../data/raw/measures/"):
    if (nrows<0):
        nrows = sys.maxsize
    f = path + file
    values = []
    time = []
    f = open(f, "r")
    i = 0
    for line in f:
        json_parsed = json.loads(line)
        values.append(json_parsed['value'])
        time.append(pd.to_datetime(json_parsed['time'], utc=True))
        i += 1
        if i >= nrows:
            break
    data_obj = {valueColName: values, 'time': pd.Series(time, name="time", dtype='datetime64[ns, UTC]')}
    return pd.DataFrame(data_obj)


def loadCsv(file, valueColName='value', nrows=-1, path="../data/raw/measures/"):
    if (nrows<0):
        nrows = sys.maxsize
    f = path + file
    dateparse = lambda dates: [pd.to_datetime(d) for d in dates]
    return pd.read_csv(f,
                       names=['sensor', valueColName, 'time'],
                       usecols=[valueColName, 'time'], header=1, nrows=nrows,
                       parse_dates=['time'],
                       date_parser=dateparse)

def saveJson(file, data, path ='../data/processed/'):
    f = path + file
    data.to_json(f, orient='records', date_format='iso', indent=2)
