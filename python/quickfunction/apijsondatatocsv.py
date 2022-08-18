import requests
import pandas as pd


r = requests.get('https://unicef.visualstudio.com/_apis/work/processes/')
#r = requests.get('https://randomuser.me/api/')

with open('events.test','w') as fd:
    fd.write(r.text)

df = pd.read_text(r'./events.json')
df.to_csv(r'./result.csv')