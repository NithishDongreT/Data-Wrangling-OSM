import xml.etree.cElementTree as ET
import pprint
import re

file = 'banglore.osm'
mapping = {'ರಾಜಗೋಪಾಲ ನಗರ ರಸ್ತೆ':'Rajagopala Nagara Road' 
            }
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

for _, element in ET.iterparse(file):
    if element.tag == "tag":
        for tag in element.iter('tag'):#iterating through multiple tags of name 'tag'...
            k = tag.get('k')
            if problemchars.search(k):#for any special charactres
                print("Wrong value->Correct Value")
                print('{}->{}'.format(k,mapping[k]))
