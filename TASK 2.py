# import packages
import numpy as np
import pandas as pd 
import requests
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

#API request
JSONContent = requests.get("https://api.magicthegathering.io/v1/cards?page= 0").json()
JSONContent2 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 101").json()
JSONContent3 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 201").json()
JSONContent4 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 301").json()
JSONContent5 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 401").json()
JSONContent6 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 501").json()
JSONContent7 =  requests.get("http://api.magicthegathering.io/v1/cards?page= 601").json()



#creating dataframe
df = pd.DataFrame(JSONContent["cards"])
df2 = pd.DataFrame(JSONContent2["cards"])
df3 = pd.DataFrame(JSONContent3["cards"])
df4 = pd.DataFrame(JSONContent4["cards"])
df5 = pd.DataFrame(JSONContent5["cards"])
df6 = pd.DataFrame(JSONContent6["cards"])
df7 = pd.DataFrame(JSONContent7["cards"])

#normalize dataframe
from pandas.io.json import json_normalize
df= pd.json_normalize(JSONContent["cards"])
df2= pd.json_normalize(JSONContent2["cards"])
df3= pd.json_normalize(JSONContent3["cards"])
df4= pd.json_normalize(JSONContent4["cards"])
df5= pd.json_normalize(JSONContent5["cards"])
df6= pd.json_normalize(JSONContent6["cards"])
df7= pd.json_normalize(JSONContent7["cards"])

#merge all the dataset in one
dataframe = pd.concat([df, df2, df3, df4, df5, df6, df7], ignore_index=True)


#DATA MANIPOLATION
df_creature = dataframe.copy()

#transform columns with list values in series
df_creature["supertypes"] = dataframe["supertypes"].apply(pd.Series)
df_subcolor = df_creature["colors"].apply(pd.Series)
df_subcolor = df_subcolor.rename(columns={0: 'main_color', 1: 'subcolor', 2 : "subcolor2", 3 : "subcolor3"})

#merge datasets
MTG_creatures = pd.concat([df_creature, df_subcolor], axis=1).drop('colors', axis=1)

#clean "non-creature" type cards(instant, enchantment,...)
df = MTG_creatures.copy()
df[['Type', 'Subtype']] = df['type'].str.split("—", 1, expand=True)

indexNames = df[df["Type"].isin(["Land", "Instant", "Enchantment" , "Sorcery" ])].index
MTG_creatures = df.drop(indexNames)  #from 700 to 467 sample size

#delete useless colums and rows
df = MTG_creatures.drop(columns = MTG_creatures.columns[[1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33]])
df = df.dropna()  #from 700 to 376 sample size

df.to_csv(r"C:\Users\loren\OneDrive\Desktop\Pythonproject_Querini\MTG.csv")


cards = pd.read_csv("MTG.csv")
