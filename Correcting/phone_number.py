import xml.etree.cElementTree as ET
import pprint
import re

#format of correct phone numbers
phone_number_format = re.compile(r'^([+][9][1]){1}([0-9]{10})$')
#phone number can contain only following elements
extract = ['+','0','1','2','3','4','5','6','7','8','9']
#extracting only permitted characters from phone number and returning new phone number
def filter_phone_numbers(phone):
    new = ''
    for char in phone:
        #if character present in extract then it is added to new string
        if char in extract:
            new += char
        else:#if character not present then it is not added..
            continue
    return new#returning new string
#verifying phone number...
def verify_phone_number(phone_number):
    #for multiple phone numbers...
    if len(phone_number) > 1:
        new_list = []
        for number in phone_number:#iterating through multiple phone number
            number = filter_phone_numbers(number)#extracting correct characters from number...
            new_list.append(number)#appending it to new list
        return ';'.join(new_list)#returnig comibined form list...
    else:
        #for single phone number
        string_phone_number = ''.join(phone_number)#converting phone number to string
        #for phone number that starts with +91 and does not have length of 13
        if string_phone_number.startswith('+91') and len(string_phone_number) != 13:
            string_phone_number = filter_phone_numbers(string_phone_number)
            if len(string_phone_number) == 13:#checking for length after filtering..
                return string_phone_number
            elif '080' not in string_phone_number[:13]:
                return string_phone_number[:13]
            else:
                n = string_phone_number.replace('080','08',1)
                return n
        elif string_phone_number.startswith('1800'):#for other cases...
                return string_phone_number
        elif string_phone_number.startswith('080'):
            string_phone_number = string_phone_number.replace('080','+91',1)
            return filter_phone_numbers(string_phone_number)
        elif len(string_phone_number) == 10:
            return '+91' + string_phone_number
        elif string_phone_number.startswith('0'):
            string_phone_number = string_phone_number.replace('0','+91',1)
            return filter_phone_numbers(string_phone_number)
        elif '(91)' in string_phone_number:
            string_phone_number = string_phone_number.replace('+(91)','+91',1)
            string_phone_number = string_phone_number.replace('(91)','+91',1)
            return filter_phone_numbers(string_phone_number)
        elif string_phone_number.startswith('80'):
            string_phone_number = string_phone_number.replace('80','+91',1)
            return filter_phone_numbers(string_phone_number)
        elif string_phone_number.startswith('91'):
            string_phone_number = string_phone_number.replace('91','+91',1) 
            return filter_phone_numbers(string_phone_number)
        else:#for any other entry
            try:
                string_phone_number = filter_phone_numbers(string_phone_number)
                string_phone_number = string_phone_number.replace('0','+91',1)
                return string_phone_number
            except:
                return string_phone_number
for _, element in ET.iterparse(file):
    for e in element:
        if e.get('k') == "phone":
            value = e.attrib['v']
            if phone_number_format.match(value):
                continue
            else:
                mul_phone_numbers = value.split(';')#spliting phone to multiple value using ;
                correct_phone_number = verify_phone_number(mul_phone_numbers)
                if len(correct_phone_number) > 13:
                    print('{}->{}'.format(mul_phone_numbers,correct_phone_number))
