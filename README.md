# Data-Wrangling-OSM

## Map Area

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
## Data Overview and Additional Ideas
  This section contains basic statistics about the dataset, 
  the SQL queries used to gather them, and some additional ideas about the data in context.
  
  ### File sizes
    banglore.osm: 52 MB
    nodes_csv: 19 MB
    nodes_tags.csv: 374 KB
    ways_csv: 3.2 MB
    ways_nodes.csv: 6.7 MB
    ways_tags.csv: 1.9 MB
    banglore.db: 35.5 MB
  
  #### No. of nodes
    SELECT COUNT(*) FROM nodes;
  232364
  
  #### No. of ways
    SELECT COUNT(*) FROM ways;
  54677
  
  #### No. of Unique Users
     SELECT COUNT(DISTINCT(e.uid)) \
            FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
  742
  
  #### Top Contributing Users
    SELECT e.user, COUNT(*) as num \
            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
            GROUP BY e.user \
            ORDER BY num DESC \
            LIMIT 10;
  [('sdivya', 15033),
  ('PlaneMad', 13196),
  ('Navaneetha', 11071),
  ('bindhu', 10585),
  ('himalay', 10403),
  ('pvprasad', 10260),
  ('subhashini', 9089),
  ('premkumar', 8952),
  ('saikumar', 7691),
  ('jasvinderkaur', 7633)]
  
  #### Number of users contributing only once
    SELECT COUNT(*) \
            FROM \
                (SELECT e.user, COUNT(*) as num \
                 FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
                 GROUP BY e.user \
                 HAVING num=1) u;
  242
  
  #### Common amenities:
    SELECT value, COUNT(*) as num \
            FROM nodes_tags \
            WHERE key="amenity" \
            GROUP BY value \
            ORDER BY num DESC \
            LIMIT 10;
  ('restaurant', 187)
  ('bank', 110)
  ('pharmacy', 68)
  ('atm', 67)
  ('place_of_worship', 66)
  ('fast_food', 63)
  ('cafe', 51)
  ('school', 44)
  ('bench', 39)
  ('hospital', 37)
  
  #### Important cuisines
    SELECT nodes_tags.value, COUNT(*) as num \
            FROM nodes_tags \
                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i \
                ON nodes_tags.id=i.id \
            WHERE nodes_tags.key="cuisine" \
            GROUP BY nodes_tags.value \
            ORDER BY num DESC \
            LIMIT 10;
  ('regional', 36)
  ('indian', 26)
  ('international', 6)
  ('pizza', 6)
  ('chinese', 5)
  ('vegetarian', 4)
  ('ice_cream', 3)
  ('meals', 2)
  ('seafood', 2)
  ('Andhra', 1)
  
  ## Conclusions
  
  The OpenStreetMap data of bangluru is of fairly reasonable quality but the typo errors caused by the human inputs are significant.
  We have cleaned a significant amount of the data which is required for this project.

1. Correcting Web site Names
    * Benifits 
        1. It is a correct way to spacify a address
        2. It will give complete address to website with protocol for protection
    * Anticipated Issue
        1. It might not be understandable by Every one.
        2. For Some people it migth be difficult to identify the address
2. Correcting Street Names
    * Benifits
        1. We will know full address or street name of the place
    * Anticipated Issue
        1. Local People migth not understand full name because they migth have used shortcut names only.
3. Correcting Phone Numbers
    * Benifits
        1. Each number will have a format that it starts with +91 and followed by 10 digits
    * Anticipated Issue
        1. Cannot differentiate between cell phone number and landline number
        2. For some people if they do not know what is +91 then they will get confused and some people migth understand only older     format.
