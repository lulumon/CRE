# Dzung Nguyen <dzungng89@gmail.com>

import os
import urllib
from PIL import Image
import xml.etree.ElementTree as etree
import unicodedata
import sys

# webpage='http://www.rejournals.com/2013/06/10/the-missner-group-completes-50000-square-foot-industrial-lease-renewal/'
webpage=sys.argv[1]

# Scraping
key='apikey=4033ff91c2109983b67559c322e7e3276ccc87cf'
url='&url='+webpage
link='http://access.alchemyapi.com/calls/url/URLGetText?'+key+url
# print link
out=urllib.urlretrieve(link,'test.xml')

doc=etree.parse('test.xml')
content=doc.find("text")
txt=unicodedata.normalize('NFD',unicode(content.text)).encode('ascii','ignore')

file=open("temp.txt","w")
file.write(txt)
file.close()



