from bs4 import BeautifulSoup as bs
import requests

URL = 'https://coursehunter.net/'
LOGIN_ROUTE = 'sign-in'

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

s = requests.session()

#csrf_token = s.get(URL).cookies['csrftoken']

login_payload = {
        'login': 'saurabhshelar90@gmail.com',
        'password': 'shubham123',
        #'csrfmiddlewaretoken': csrf_token
        }

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
main_url="https://coursehunter.net/course/javascript-stan-senior-frontend-razrabotchikom"
print(login_req.status_code)

cookies = login_req.cookies


with requests.Session() as s:
    d=s.get(main_url, headers=HEADERS)
    test = s.post(URL, headers=HEADERS, data=login_payload)
    print(d.text)

#soup = bs(s.get(URL + 'watchlist').text, 'html.parser')
""""
tbody = (soup.find(class_="course-figure"))
print(tbody)
"""


