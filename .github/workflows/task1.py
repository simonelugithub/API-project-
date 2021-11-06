# import packages
import pandas as pd 
import requests
import json

#API request
JSONContent = requests.get("https://api.magicthegathering.io/v1/cards").json()

#Json normalization
df =pd.DataFrame(JSONContent["cards"])
from pandas.io.json import json_normalize
pd.json_normalize(JSONContent["cards"])

#clean usefull columns
df = df.drop(columns = df.columns[[4,6,7,9,13,16,18,19,20,21,28,27,26,25,23,22]])
df = df.fillna(0)

#write csv file
df.to_csv(r"C:\Users\loren\OneDrive\Desktop\Pythonproject_Querini\MGT.csv")
