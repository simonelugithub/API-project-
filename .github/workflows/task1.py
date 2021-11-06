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
