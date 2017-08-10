import xml.etree.cElementTree as ET
import pprint
import re
import sys

file = 'banglore.osm'
#Exceptions for words in street whose length is less than 3
exception = ['&','BMS','Bee','BT','BTM','Bus','C.V','Bed','CBI','Car','And',"D'",'DOS','DV','Dr.','End','Eye','GM',
             'GR','HAL','HBR','Joy','KGA','KH','KHB','KLE','LIC','MC','Mm','MT','N.','NG','New','No.','OTC','Off','Old',
             'RK','RMZ','RPC','Raj','Ram','Rao','Roy','SBM','Sai','sai','Sri','To','TC','UB','Urs','Via','Web','and','car','hp',
             'of','th','to','CMH']
alphabet = re.compile(r'^([a-z]|[A-Z])$')#For comparing all Occurrence of Single character
alpha_digit = re.compile(r'^([0-9]+)([a-z]|[A-Z]|,)*$')#For comparing of digits followed by Alphabets
#For correcting shortcuts to correct forms...
mapping = {'Ad':'And','I':'1st','II':'2nd','III':'3rd','IV':'4th','CHM':'Chinmaya Mission Hospital','CV':'C.V.',
           'BSK':'Banashankari','Bsk':'Banashankari','DVG':'DV Gundappa','Dr':'Dr.','Hal':'HAL','Ist':'1st','J.':'J',
           'Jct':'Junction','MG':'Mahatma Gandhi','MRR':'M Rama Roa',',Mm':'Mm','No':'No.','Opp':'Opposite','opp':'Opposite',
           'Rd':'Road','Rd,':'Road','St':'Street','St.':'Street','St,':'Street','WOC':'West of chord road'}
i = 0
correct_words = []
for _, element in ET.iterparse(file):
    for e in element:
        if e.get('k') == "addr:street":
            value = e.attrib['v']
            if value.startswith(','):#If value stats with ',' then we have to replace..
                value = value.replace(', ','')
            words = value.split(' ')#Splitting Street name into words.
            while '' in words:#if words have empty character in them then we have to remove those characters
                words.remove('')
            while ',' in words:#if words have ',' in them then we have to remove that character and append it to previous word
                i = words.index(',')#finding index of wrong word
                words.remove(',')#Removing ',' character
                words[i-1] += ','#appending ',' to previous word
            for word in words:#iterating over individual word
                if len(word) <= 3:#correcting word only if it's length is less than 3
                    if alphabet.match(word) and word not in exception:#if word matches expression then added to exception
                        exception.append(word)
                        continue
                    if alpha_digit.match(word) and word not in exception:#if word matches expression then added to exception
                        exception.append(word)
                        continue
                    if word in mapping:#if word is in mapping then it is corrected
                        i = words.index(word)#finding index of wrong word
                        words[i] = mapping[word]#Overriding wrong word with correct word in words
                    elif word in exception:#if word in exception then continuing the loop
                        continue
                if value != ' '.join(words) and ' '.join(words) not in correct_words:
                    correct_words.append(' '.join(words))
                    print('{} -> {}'.format(value,' '.join(words)))
                    i += 1
                    if i < 10:
                        continue
                    else:
                        sys.exit()
