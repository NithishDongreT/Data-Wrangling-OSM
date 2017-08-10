# Data-Wrangling-OSM

### Map Area

[Bangaluru](http://overpass-api.de/api/map?bbox=77.5044,12.9305,77.6788,13.0280),India

The above link will give the area of Bangaluru to download in format of OSM.
Also above map is of my hometown, so I’m more interested to see what database querying reveals.

## Problems Encountred in the map
  After auditing the map area i have encountered following problmes.

1. As per Audited key names we have one key name which is in special characters.
2. Problem with postal code is it does not starts with 560 and there might be any error while enterring data as 650 instead of 560 and maybe entered extra character with digits of postal codes
3. Problem with house number is that it has a string as No to represent a number and it has more alphabets for a house number
4. Problem with street names that in my local area there is no exact division of area names as street, city. Hence the whole address is ginven in the place of street. Therfore I have checked for Shortcuts in name to be replaced by the exact form.
5. Problem with Phone number is thatit should start with +91. It should not have any spaces or extra symbols.
6. Problem with websites is that it does not specify full url path or most of them do not specify protocol.
