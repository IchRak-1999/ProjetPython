import pandas as pd

def readData(fileName):
    data = pd.read_excel(fileName)
    return data
    """
    print(data["Région"])
    """

def mapDepitRegion():
    data = readData("nombre_debit_departement.xlsx")
