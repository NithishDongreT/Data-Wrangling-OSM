import sqlite3
import xml.etree.cElementTree as ET
import csv
import codecs
from unittest import TestCase
import cerberus
import schema

con = sqlite3.connect("banglore.db")
con.text_factory = str
cur = con.cursor()

# create nodes table
cur.execute("CREATE TABLE if not exists nodes (id, lat, lon, user, uid, version, changeset, timestamp);")
with open('nodes.csv','r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) \
             for i in dr]

cur.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()

#create nodes_tags table
cur.execute("CREATE TABLE if not exists nodes_tags (id, key, value, type);")
with open('nodes_tags.csv','r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in dr]

cur.executemany("INSERT INTO nodes_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
con.commit()

#Create ways table
cur.execute("CREATE TABLE if not exists ways (id, user, uid, version, changeset, timestamp);")
with open('ways.csv','r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in dr]

cur.executemany("INSERT INTO ways (id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()

#Create ways_nodes table
cur.execute("CREATE TABLE if not exists ways_nodes (id, node_id, position);")
with open('ways_nodes.csv','r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'], i['node_id'], i['position']) for i in dr]

cur.executemany("INSERT INTO ways_nodes (id, node_id, position) VALUES (?, ?, ?);", to_db)
con.commit()

#Create ways_tags table
cur.execute("CREATE TABLE if not exists ways_tags (id, key, value, type);")
with open('ways_tags.csv','r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in dr]

cur.executemany("INSERT INTO ways_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
con.commit()
