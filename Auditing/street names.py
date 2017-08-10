import xml.etree.cElementTree as ET
import pprint
import re

filename = 'sample20.osm'

#Auditing for Street Names...
def street_names_audit(file_name):
    wrong_words_in_street = dict()
    for _, element in ET.iterparse(file_name):
        for e in element:
            if e.get('k') == "addr:street":
                value = e.attrib['v']
                words = value.split(' ')#Splitting Street name into words.
                for word in words:
                    if len(word) <= 3:
                        #For every word who's length is less than 3 then 
                        #count for that word is increased in wrong_words_in_street
                        if word in wrong_words_in_street:
                            wrong_words_in_street[word] = wrong_words_in_street[word] + 1
                        else:
                            wrong_words_in_street[word] = 1            
    return wrong_words_in_street
wrong_words_in_street = street_names_audit(filename)
for word in wrong_words_in_street:
    #if the count of repetition is greater than 5 then it will print those names and their values
    if wrong_words_in_street[word] >= 5:
        print('{}->{}'.format(word,wrong_words_in_street[word]))
