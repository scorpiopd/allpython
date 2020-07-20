import requests
url ="https://icanhazdadjoke.com/"
response=requests.get(url,headers={"Accept":"text/plain"})
jresponse=requests.get(url,headers={"Accept":"application/json"})
print(response.text)
data=jresponse.json()
print(jresponse.text)
print(data["joke"])