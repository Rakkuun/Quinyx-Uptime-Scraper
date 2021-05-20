import requests
from bs4 import BeautifulSoup
from datetime import datetime

# get HTML from SmartRecruiters status page
page = requests.get("http://status.smartrecruiters.com/")

# parse HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# get current status string from page-status element
current_status = soup.find('div', class_='page-status').get_text(strip=True)

# define no reported issue in a variable
system_has_no_issues = "All Systems Operational"

# set current time
now = datetime.now()

# check if current status equals system has no issues & report back
if current_status == system_has_no_issues:
    print(now, ": SmartRecruiters reports no issues at this time.")
else:
    print(now, ": ALARM: SmartRecruiters has reported issues! Visit http://status.smartrecruiters.com/ for more information.")