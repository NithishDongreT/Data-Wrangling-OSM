# Data-Wrangling-OSM

### Map Area

[Bangaluru](http://overpass-api.de/api/map?bbox=77.5044,12.9305,77.6788,13.0280),India

The above link will give the area of Bangaluru to download in format of OSM.
Also above map is of my hometown, so I’m more interested to see what database querying reveals.

## Problems Encountred in the map
  After auditing the map area i have encountered following problmes.

1. As per Audited key names we have one key name which is in special characters.
   
   Output of auditong keys gives following output
      ```
      Others:-fuel:octane_95:yes
      Others:-fuel:octane_98:yes
      Others:-shop_1:confectionery
      Others:-phone_1:080 23207729
      Problem:-ರಾಜಗೋಪಾಲ ನಗರ ರಸ್ತೆ:ದಾಸರಹಳ್ಳಿ ಕೆರೆ
      Others:-name_1:NR Colony
      Others:-alt_name_1:Srinagar - Kanyakumari Highway
      Others:-alt_name_2:Delhi - Chennai Highway
      {'lower': 16234, 'lower_colon': 1091, 'other': 7, 'problemchars': 1}
      ```
2. Problem with postal code is it does not starts with 560 and there might be any error while enterring data as 650 instead of 560 and maybe entered extra character with digits of postal codes
    
    Output of auditong postal codes gives following output
    ```
    ['570008', '560072,', '650027']
    ```
3. Problem with house number is that it has a string as No to represent a number and it has more alphabets for a house number
    
    Output of auditong house number gives following output
    ```
    45, 3rd Main, M M Layout, Kavalbyrasandra
    #93,  IIIrd Floor, Salarpuria Business Center
    G03, G04
    UG07, UG08
    Lake Road
    1 Main Road 
    14 Ashoknagar
    Ashoknagar
    Ashoknagar
    No. 26/10, Banaswadi Main Road, Banaswadi Layout, Maruthi Sevanagar
    ,CB-01,1st Floor
    No. 26/10, Banaswadi Main Road, Banaswadi Layout, Maruthi Sevanagar
    No. 26/10, Banaswadi Main Road, Banaswadi Layout, Maruthi Sevanagar
    ```
4. Problem with street names that in my local area there is no exact division of area names as street, city. Hence the whole address is ginven in the place of street. Therfore I have checked for Shortcuts in name to be replaced by the exact form.
    
    Output of auditong street names gives following output with number of times it has repeated
    ```
    100->9
    K->6
    2nd->20
    6th->11
    8th->5
    80->5
    5th->11
    4th->13
    1st->15
    9th->10
    Rd,->13
    ,->7
    ```
5. Problem with Phone number is thatit should start with +91. It should not have any spaces or extra symbols.
    
    Output of auditong phone number gives following output.
    ```
    +91-80-41139572
    +91 80 25205305
    +91-80-40441234; +91-80-39884433
    +91-80-4155-4695
    +91 80 2338 1707
    +918022240289, +918022210309
    +91-96327 00311
    1800 3000 8866
    "080 4180 9000 "
    +91 94481 67969
    +91 80507 82573
    +91 97310 15011
    +9181518 34646
    (91)-9901650250
    +91 96118 59911
    "096321 55362 "
    +91 80 2530 4477
    +91 80 4120 2478
    +91 9886921292
    ```
6. Problem with websites is that it does not specify full url path or most of them do not specify protocol.
    
    Output of auditong phone number gives following output.
    ```
    mcafee.com
    angelsclinic.in
    santoshhealthcare.com
    diavista.co.in
    kaatizone.com
    balpharma.com
    micatapes.net
    voltasac.com
    sportslineindia.com
    uspoloassn.com
    rootsfitness.co.in
    rotork.com
    Www.hajiameengroup.in
    ```
