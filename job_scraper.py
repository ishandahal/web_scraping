from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.indeed.com/jobs?q=Entry%20Level%20Machine%20Learning&l&ts=1609087830269&rq=1&rsIdx=3&fromage=last&newcount=769&advn=8876452989351355&vjk=8759116ae6756433").text
soup = BeautifulSoup(page, 'html.parser')


company_name = soup.find('div', class_="sjcl").text.lstrip()
print(company_name)

