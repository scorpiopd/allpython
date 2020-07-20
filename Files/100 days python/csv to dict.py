from urllib.request import urlretrieve
from collections import namedtuple
from csv import reader


import requests

data_url = 'https://storage.googleapis.com/kagglesdsdata/datasets/573696/1039362/AYUSHHospitals.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1586022365&Signature=mXGuVTY5VfxAmsXHYLJbgCBen0KobN3D3x87qMxJhOHV1CJNe9nRVo6pXK1PKMFxC%2Bmu485hUWawQlxGzUfRJfk76etakC9IndyOl4eEwFlC4DzOPhC7sISbRoOf1bKQQ9NdKLCATB42q05aWl4YrbvZ4tbqQOJ%2F1CWUmFcB6%2FjMTaXKZO3aY9uhVt02qVS9I%2BhxOdrDRLtwtBqZkSNqS4K4m3GC%2BT063hVdiR4TQo%2BBtzvsTHzn4rr1NxHFszfYKpC9%2Bisl2yv%2B%2BcJHmBBsMvHrhTuMrqHfcTqkk4dvUvQhjqNkYdhBzkUAYkNzjsZT%2FzftPWIzj3WtLhUPRLIixg%3D%3D&response-content-disposition=attachment%3B+filename%3DAYUSHHospitals.csv'
#data_url = "https://www.kaggle.com/dheerajmpai/hospitals-and-beds-in-india/download/p19XqYl1AEyrwrOQLN3F%2Fversions%2Ffz4wUZhpTaO6mfzMlDyP%2Ffiles%2FAYUSHHospitals.csv?datasetVersionNumber=1"

r = requests.get(data_url)
store=r.text
print(store)
v=''
#will convert it to list
v = list(zip(v, store))

print(v)


# r = requests.get(data_url,headers={"Accept":"application/json"})

# print(r.text)
# gives back source code giant HTML made for human eyes


# includes all the metadata that returned
# print(r.headers)




