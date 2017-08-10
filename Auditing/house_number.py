import xml.etree.cElementTree as ET
import pprint
import re

filename = 'sample20.osm'
#Auditing for house numbers...
def check_house_number(house_number):
    #if house number is not integer thenreturs false or returns true.
    try:
        int(house_number)
        return True
    except ValueError:
        return False 
wrong_house_number = []
correct_house_number = []
for _, element in ET.iterparse(filename):
    for e in element:
        if e.get('k') == "addr:housenumber":
            if not check_house_number(e.attrib['v']):
                wrong_house_number.append(e.attrib['v'])
            else:
                correct_house_number.append(e.attrib['v'])
for number in wrong_house_number:
    #if the length of house number is greater than 5 then it will print those numbers and those will have most of the problems
    if len(number) > 5:
        print(number)
