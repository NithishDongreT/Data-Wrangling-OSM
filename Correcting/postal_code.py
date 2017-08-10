import xml.etree.cElementTree as ET
import pprint
import re

file = 'banglore.osm'
#Correcting Postal codes...
def correct_postal_code(postal_code):
    new_code = ''
    mapping = {'79':'560079',
                '56005':'560005'
              }
    #Checking for mistakes while entering code as 650 instead of 560
    if  not postal_code.startswith('560') and len(postal_code) == 6:
        return '560' + postal_code[-3:]
    elif len(postal_code) > 6:#checking if code has length more than 6  then removing extra entries.
        for digit in postal_code:
            try:
                int(digit)
                new_code += digit
            except ValueError:
                continue
        return new_code
    elif len(postal_code) < 6:#if code has length less than 6 then returning the corrected code.
        return mapping[postal_code]
                
            
for _, element in ET.iterparse(file):
    for e in element:
        if e.get('k') == "addr:postcode":
            postal_code = e.attrib['v']
            if postal_code.startswith('560') and len(postal_code) == 6:
                continue
            else:
                new_postal_code = correct_postal_code(postal_code)
                print('{}->{}'.format(postal_code,new_postal_code))
