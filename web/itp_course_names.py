from BeautifulSoup import BeautifulSoup
import urllib

url = "https://itp.nyu.edu/registration/CourseListing.php?semester=Fall&year=2011"

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

course_tags = soup.findAll('h3')
for course_tag in course_tags:
  print course_tag.string.strip()

