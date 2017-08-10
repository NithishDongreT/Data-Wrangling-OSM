import sqlite3
import pprint

#Connecting to database
con = sqlite3.connect("banglore.db")
#creating a cursor for executing sql statements
cur = con.cursor()

#testing whether query retrieves or working correctlly.
result = cur.execute('SELECT COUNT(*) FROM nodes')
print(result.fetchone()[0])

#trying to find no. of all ways in map area
result = cur.execute('SELECT COUNT(*) FROM ways')
print(result.fetchone()[0])

#Number of unique users
result = cur.execute('SELECT COUNT(DISTINCT(e.uid)) \
            FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e')
print(result.fetchone()[0])

#Top contributing users
users = []
for row in cur.execute('SELECT e.user, COUNT(*) as num \
            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
            GROUP BY e.user \
            ORDER BY num DESC \
            LIMIT 10'):
    users.append(row)
pprint.pprint(users)

#Number of users contributed only once
result = cur.execute('SELECT COUNT(*) \
            FROM \
                (SELECT e.user, COUNT(*) as num \
                 FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
                 GROUP BY e.user \
                 HAVING num=1) u')
print(result.fetchone()[0])

#Common amneties
for row in cur.execute('SELECT value, COUNT(*) as num \
            FROM nodes_tags \
            WHERE key="amenity" \
            GROUP BY value \
            ORDER BY num DESC \
            LIMIT 10'):
    print(row)

#faviorite cuisine 
for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num \
            FROM nodes_tags \
                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i \
                ON nodes_tags.id=i.id \
            WHERE nodes_tags.key="cuisine" \
            GROUP BY nodes_tags.value \
            ORDER BY num DESC \
            LIMIT 10'):
    print(row)
