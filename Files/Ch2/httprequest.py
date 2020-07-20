import requests

url = "http://www.google.com"
response = requests.get(url)
print(f"your request to {url} came back with statuscode {response.status_code} ")












"""""""""""
import requests
res =requests.get("https://news.ycombinator.com/")
print(res)# here we are seeing response code
print(res.ok)
print(res.headers)# prints out all the meta data that came back
"""""""""
