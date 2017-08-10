import xml.etree.cElementTree as ET
import pprint
import re
import validators as v

filename = 'sample20.osm'
for _, element in ET.iterparse(filename):
    for e in element:
        if e.get('k') == "website":
            if not v.url(e.attrib['v']) and not e.attrib['v'].startswith('www'):
                #normal url starts with protocol then followed by domain...
                #if it does not have any of these then we will have problem
                print(e.attrib['v'])
