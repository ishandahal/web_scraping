import requests
from bs4 import BeautifulSoup

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "html.parser")

job_dict = {}

# collects all individual cards
containers = soup.findAll('li', class_="clearfix job-bx wht-shd-bx")
# iterate each card and grab job title, key skills and link to info
# create a dict with the above information
for container in containers:
    job_title = container.find("h3", class_="joblist-comp-name").text.strip()
    key_skills = container.find("span", class_="srp-skills").text.strip().split(",")
    link_with_details = container.h2.a['href']
    job_dict[job_title] = key_skills
    job_dict[job_title].append(link_with_details)

print(len(job_dict))
print(job_dict["3RI Technologies Pvt Ltd"])




