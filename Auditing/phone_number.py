import xml.etree.cElementTree as ET
import pprint
import re

filename = 'sample20.osm'
#auditing phone number...
tag_phone_number = []
for _, element in ET.iterparse(filename):
    for e in element:
        if e.get('k') == "phone":
            tag_phone_number.append(e.attrib['v'])
for phone_number in tag_phone_number:
    #in india the default phone number length is 13 and if it is greater than 13 then we have problem in data
    if len(phone_number) > 13:
        print(phone_number)
