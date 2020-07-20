import requests
import soup as soup
from bs4 import BeautifulSoup
import csv

response = requests.get("https://coursehunter.net/frontend/javascript")
soup = BeautifulSoup(response.text, "html.parser")
#articles = soup.find_all("article")
#print(articles)
# for article in articles:
# print(soup.body.div)

#d = (soup.find(class_="course-figure"))

#d = soup.find_all("picture", class_="course-figure")

#d = soup.select(".course-figure")

d = soup.find_all("picture", {"class": "course-figure", "data-link": True})
for d in soup.findAll(attrs= {"class":"course-figure"}):


    print(d["data-link"])

#d = soup.find_all(attrs={"data-link":True})

# d= soup.find_all('course-figure').get('data-link')

#print(d)

"""m = []
m = d.copy()
single = list(map(str, m))
print(single)"""
