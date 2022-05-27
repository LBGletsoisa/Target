import urllib
import re
from bs4 import BeautifulSoup

datafromwebsite=urllib.urlopen("https://api.thingspeak.com/channels/289288/feeds.json?results=1");
select=repr(datafromwebsite.read());
select=select[300:];

pick=re.search('field1":"(.+?)",',select);
if pick:
 print pick.group(1);

