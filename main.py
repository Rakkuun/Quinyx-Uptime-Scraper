import requests
from bs4 import BeautifulSoup

# get HTML from SmartRecruiters status page
page = requests.get("http://status.smartrecruiters.com/")

# parse HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# get current status string from page-status element
current_status = soup.find('div', class_='page-status').get_text(strip=True)

system_has_no_issues = "All Systems Operational"

if current_status in system_has_no_issues:
    print("All systems should work just fine!")
else:
    print("ALARM: System is experiencing issues!")