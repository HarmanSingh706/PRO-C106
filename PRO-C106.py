import plotly.express as px
import csv
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marksInPercentage = []
    daysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x" : marksInPercentage, "y": daysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present:\n ",correlation[0,1])

def setup():
    dataPath  = "./data/Student Marks vs Days Present.csv"

    datasource = getDataSource(dataPath)
    findCorrelation(datasource)
    plotFigure(dataPath)

setup()