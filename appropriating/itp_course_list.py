import sys
from bs4 import BeautifulSoup
import urllib

semester, year = sys.argv[1:]

url = "https://itp.nyu.edu/registration/CourseListing.php?" + \
		urllib.urlencode({'semester': semester, 'year': year})

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

for tag in soup.findAll('h3'):
  table = tag.findNextSibling('table')
  tds = table.findAll('td')
  instructor = tds[2].contents[0]
  print tag.string.strip() + "\t" + instructor.strip()

