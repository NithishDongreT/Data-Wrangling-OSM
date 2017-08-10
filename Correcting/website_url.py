import xml.etree.cElementTree as ET
import pprint
import re
#for validating url using following package
import validators as v

file = 'banglore.osm'
#function for correcting normal errors
def correct_url(path):
    if 'NA' in path:#if they gave Not Available or 'NA' for website value
        return None
    if path.startswith('www'):#if path starts with www
        path = 'https://' + path#adding https to beginning
        if v.url(path):#validating corrected path
            return path
    else:
        path = 'https://www.' + path#for other cases...
        if v.url(path):
            return path
i = 0
for _, element in ET.iterparse(file):
    for e in element:
        if e.get('k') == "website":
            value = e.attrib['v']
            if v.url(value):#if value is correct then iterating to next value
                continue
            else:#if not then value is given for correction and old value is over written by new value
                new_value = correct_url(value)
                if not value.startswith('www') and i <= 10:
                    print('{} -> {}'.format(value,new_value))
                    i += 1
