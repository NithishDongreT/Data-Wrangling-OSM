#Auditing for Postal Codes...
def check_postal_code(postal_code):#function used to check postal codes...
    if postal_code.startswith('560'):#to check if code starts with 560...
        try:
            int(postal_code)#to check if postal code can be converted integer...
            return True
        except ValueError:
            return False
    else:
        return False
def postal_code_audit(file_name):#function for auditing postal codes...
    wrong_postal_codes = []
    for _, element in ET.iterparse(file_name):
        for e in element:
            if e.get('k') == "addr:postcode":
                if not check_postal_code(e.attrib['v']):
                    wrong_postal_codes.append(e.attrib['v'])#printing postal code if it has any problems..
    return wrong_postal_codes
wrong_postal_codes = postal_code_audit(filename)
print(wrong_postal_codes)
