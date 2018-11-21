###
### Trying to extract a comprehensive sheet list from Fieldlens via webscraping
###

### Drawing name
### class="drawing--plan-name ng-binding ng-scope"

### Drawing number
### class="name--label"



import requests
from bs4 import BeautifulSoup as bsoup

seattle = requests.get('https://app.fieldlens.com/project/128494/we-live-2031-3-rd-ave/drawings', auth=('chris.chan@wework.com', 'HoleSovi#7'))
print(seattle.status_code)

seattle_soup = bsoup(str(seattle), 'html.parser')
print(str(seattle_soup))

print(seattle_soup.find("name--label"))