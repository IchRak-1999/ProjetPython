import pandas as pd
import csv

def readData():
    print('Function Data')

    with open("data.xlsx", 'r') as input:
        reader = csv.DictReader(input)
        print(reader)

readData()