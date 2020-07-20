import requests

data_url = "https://storage.googleapis.com/kagglesdsdata/datasets/573696/1039362/AYUSHHospitals.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1586025356&Signature=B9AMrAZRr9ODQoav%2BKwDSLwXfNG0NYkcZELo%2BtlSo0V0l8pw%2FqhjVIMijfPpLDlwgwQFmdQNov1LADR8YrnZE8K4pRcko1aDOP%2FrCpc76ZoAYAGfUGhXb42okuWUhm%2FXJE0Bu9V6VUFyNGDxVt%2BET4ql0vn8E1Czs%2FJjAhUy7kHcRZfdtreovgPu3Vm92Ar1HxIy3zSxEn1jEfqVf6Wtnuofyv9HJ58uQ863zx9red3%2F2QdydjyQJj9lYjmd25LpXCPJNkmi%2FpcwwsZB6V2%2FS8h5fjuFTfJhDUhc5Z7p%2FADPu9U4TN4iqISJydaJa2JaBMDA5DkojyC5gcIaf9%2B2Aw%3D%3D&response-content-disposition=attachment%3B+filename%3DAYUSHHospitals.csv"  # The direct link to the




r = requests.get(data_url)  # Attempts to download the CSV file. Gets rejected because we are not logged in.

f = open('AYUSHHospitals.csv', 'wb')  # Writes the data to a local file one chunk at a time
for chunk in r.iter_content(chunk_size=512 * 1024):  # Reads 512KB at a time into memory
    if chunk:  # filter out keep-alive new chunks
        f.write(chunk)
f.close()

print(r)


from csv import reader

with open("AYUSHHospitals.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(f"{row[1]} has {row[2]} Hospitals")


#https://github.com/mahumt/Tidbits/blob/master/downloading%20from%20kaggle%20using%20python.py
#additional links https://medium.com/@whitelotus/python-error-typeerror-write-argument-must-be-str-not-bytes-730714328ebd