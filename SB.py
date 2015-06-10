# Next Step: This script should output the state (right now only AK), a list of cities in AK as listed, and the php url to call that page.
# Ie:
# Alaska, Anchorage, city.php?CITY=Anchorage&stateID=2
# Alaska, Bettles, city.php?CITY=Bettles&stateID=2

# More features to come later - more goodies too
# This script doesn't seem to work in python 3.4. urllib2 seems to cause issues
import urllib2
from bs4 import BeautifulSoup
import re

#url = "http://www.loc.gov/rr/geogmap/sanborn/states.php?stateID=2&Submit=SEARCH" #Original URL for states page
url = "http://www.csun.edu/~ssk35332/SanbornAK.html"
#url = "http://www.csun.edu/~ssk35332/SanbornAnch.html"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

#for link in soup.find_all('a'):
#    if str(link.get('href')) != 'None':
#        print(link.get('href'))

for link in soup.find_all('td'): #this is (td) the most succesful find_all yet. Just need to weed it out so it only returns 
#    if str(link.get('a')) != 'None':
#    print (link.string)
    print (link.a)
#        print(link.get('href'))
#    else:
#        print "nothing found"

#soup = soup.find_all(class_ = 'alternatetr') #don't know why this class selection doesnt work

