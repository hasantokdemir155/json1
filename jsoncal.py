import requests
import pandas as pd
import json




#print(sonc.text)[]


sonc=pd.read_json('dn.json')
sonc1=sonc









soncx=sonc1['id']
print(sonc1['batters'][0]['batter'][3]['type'])
print(sonc1['topping'][0][0]['id'])
print(sonc1['id'])
print(sonc1['batters'][2]['batter'][1])
print(sonc1['topping'][2][2]['type'])
snc=sonc1['batters']
print(type(snc))
    
for i in range(0,3):
    print(sonc1['batters'][i])
    
