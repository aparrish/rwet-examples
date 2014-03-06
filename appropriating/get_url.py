import urllib
import sys

url = sys.argv[1]
urlobj = urllib.urlopen(url)
data = urlobj.read()
print data
