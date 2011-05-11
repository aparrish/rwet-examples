from BeautifulSoup import BeautifulSoup
import urllib

url = "https://itp.nyu.edu/registration/CourseListing.php?semester=Fall&year=2011"

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

for tag in soup.findAll('h3'):
  table = tag.findNextSibling('table')
  tds = table.findAll('td')
  instructor = tds[2].contents[0]
  print tag.string.strip() + "\t" + instructor.strip()

