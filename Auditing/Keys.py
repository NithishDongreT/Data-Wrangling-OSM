import xml.etree.cElementTree as ET
import pprint
import re


filename = 'sample20.osm'
#3 regular expressions to compare the key
lower = re.compile(r'^([a-z]|_)*$')#To check if key has only alphabets or underscore
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')#To check if key has multiple : symbols 
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')#If key has any special characters...

#Decides type of each key...
def key_type(element, keys):
    if element.tag == "tag":#to check whether key belongs to tag named 'tag'...
        for tag in element.iter('tag'):#iterating through attributes of name 'tag'...
            k = tag.get('k')
            if lower.search(k):#checking whether key is having lower case or not...
                keys['lower'] += 1
            elif lower_colon.search(k):#checking whether key is devided with another : symbol...
                keys['lower_colon'] += 1
            elif problemchars.search(k):#for any special charactres
                keys['problemchars'] += 1
                print('Problem:-{}:{}'.format(tag.get('k'),tag.get('v')))#print those special keys...
            else:
                keys['other'] += 1#mostlly if key had numbers they will be other...
                print('Others:-{}:{}'.format(tag.get('k'),tag.get('v')))
                        
    return keys

def process_map(file_name):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    
    for _, element in ET.iterparse(file_name):
        keys = key_type(element, keys)

    return keys

keys = process_map(filename)
pprint.pprint(keys)
