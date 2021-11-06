# import packages
import pandas as pd 
import requests
import json

#API request
JSONContent = requests.get("https://api.magicthegathering.io/v1/cards").json()

