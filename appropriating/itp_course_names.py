import sys
from bs4 import BeautifulSoup
import urllib

semester, year = sys.argv[1:]

url = "https://itp.nyu.edu/registration/CourseListing.php?" + \
		urllib.urlencode({'semester': semester, 'year': year})

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

course_tags = soup.findAll('h3')
for course_tag in course_tags:
  print course_tag.string.strip()

