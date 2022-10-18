import requests
from bs4 import BeautifulSoup
import pandas

headline =[]
des = []
url = "https://www.bbc.com/"
accepted_Not = requests.get(url)
if accepted_Not.status_code == 400 or accepted_Not.status_code == 401 or accepted_Not.status_code == 402 or accepted_Not.status_code == 403 or accepted_Not.status_code == 402 :
    print("Something Went Wrong")
    exit(0)
else:
    data = accepted_Not.content
    pretty = BeautifulSoup(data, "html.parser")
    fetch = pretty.find_all("a", class_="media__link")
    fetch2 = pretty.find_all("p", class_="media__summary")

    for a in fetch:
        headline.append(a.get_text())
    for a in fetch2:
        des.append(a.get_text())

print(len(headline))
print(len(des))
# newsDict = {"HeadLine" : headline, "Description" : des}
# table = pandas.DataFrame(newsDict)
# print(table)


