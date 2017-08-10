import xml.etree.cElementTree as ET
import pprint
import re

file = 'banglore.osm'
#Exceptions for house numbers because some of the house have letters in their numbers or a building is used to identify a shop..
exception = ['RMZ Infinity','LG-34','UG','23 & 24','Office','1st floor','1st Floor','3rd Floor','3547A','G28','G30',
             'G11','G27','UG04','UG17','UG23','UG27','UG34','UG38','3A','648N','648B','648D','846A','842A','House 5',
             '777P','Garuda Mall','Lake Road','UG 67 & 69','43-B','216B','74 & 75','E 77','Prestige No.1','Office No 10',
             '42-43','The Forum','3302L']
def correct_house_number(house_number):
    #Splitting is for most house numbers in this map have given multiple values seperated by ,
    house_num = house_number.split(',')
    #if house number is alphabet then just return None
    if house_number.isalpha():
        return None
    #if the house number has # or / then we can accept as a house number
    elif '#' in house_number or '/' in house_number:
        #for replacing any occurence of No for number...
        if 'No' in str(house_number):
            return house_num[0].replace('No. ','').replace('No.','').replace('No ','')
        else:
            return house_num[0]
    #for value that has multimple entries then returning correct value
    elif len(house_num) != 1:
        #for 1st entry in list if its not empty
        if len(house_num[0]) != 0:
            #for 1st entry in list if it does not contain no
            if not 'No' in str(house_num[0]):
                return str(house_num[0])
            #for 1st entry in list if it does not contain no
            else:
                new_number = str(house_num[0])
                return new_number.replace('No ','').replace('No.','')
        #for 1st entry in list if its empty
        else:
            return str(house_num[1])
    #for value that has single entry then returning correct value
    else:
        #checking for exceptions
        if str(house_num[0]) in exception:
            return str(house_num[0])
        #if value has No in them
        elif 'No' in str(house_num[0]):
            new_number = str(house_num[0])
            new_number = new_number.replace('No ','').replace('No.','').replace('No-','').replace('N0.','').replace('No','')
            return new_number.replace(' ','').replace('no:','')
        #for any other entry that does not fits any condition..
        else:
            return None
            
for _, element in ET.iterparse(file):
    for e in element:
        if e.get('k') == "addr:housenumber":
            house_number = e.attrib['v']
            try:#checkig for value is with only digits 
                int(house_number)
                continue
            except ValueError:#for value error we have to correct those numbers
                new_house_number = correct_house_number(house_number)
                #if the length of house number is greater than 20 then it will print those numbers and their corrected values
                if len(house_number) > 20:
                    print('{}->{}'.format(house_number,new_house_number))
