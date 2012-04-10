from bs4 import BeautifulSoup
from random import choice
from time import sleep
import sys
import urllib
import re

# here's how to fake a user agent string with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
urllib._urlopener = FakeMozillaOpener()

# get term from command line; put together a URL; determine the first letter
# of the term
term = sys.argv[1]
url = 'http://en.wikipedia.org/wiki/' + term
first_let = term[0].lower()

# keep track of links we've already seen
already_seen = set()

print term

while True:

  # grab HTML from the current URL; find the bodyContent div
  data = urllib.urlopen(url).read()
  soup = BeautifulSoup(data)
  content = soup.find('div', attrs={'id': 'bodyContent'})

  # next_tags will contain BeautifulSoup tag objects for all <a> tags that
  # have (a) an 'href' attribute; (b) have a 'title' attribute; (c) link to
  # an internal Wikipedia page; and (d) have a 'title' attribute whose
  # first letter matches the first letter of the term used to begin the
  # process. 
  next_tags = list()
  for a_tag in content.findAll('a', attrs={'href': True, 'title': True}):
    title = a_tag['title']
    if re.search(r"^/wiki/", a_tag['href']) and title[0].lower() == first_let:
      next_tags.append(a_tag)

  # quit if no matching <a> tags were found
  if len(next_tags) == 0:
    break

  # get a random next tag; quit if we've already seen this tag; add to the
  # already_seen set (to prevent looping)
  next_tag = choice(next_tags)
  if next_tag['title'] in already_seen:
    break
  already_seen.add(next_tag['title'])

  # display this tag's title; set the url variable to the next page to grab
  # from wikipedia; sleep for a second (to not be a jerk to the wikipedia
  # servers)
  print next_tag['title']
  url = 'http://en.wikipedia.org' + next_tag['href']
  sleep(1.0)

