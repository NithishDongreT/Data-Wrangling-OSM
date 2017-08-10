#helps to identify important tag keys in the sample data.
#Here we will ctreat a dictionary holding key as key name and value as number of times it has appeard.
import xml.etree.cElementTree as ET
import pprint
import re

filename = 'sample20.osm'
node_tag_keys = dict()
for _, element in ET.iterparse(filename):
    if element.tag == 'node':
        for e in element:
            if e.attrib['k'] in node_tag_keys:
                node_tag_keys[e.attrib['k']] += 1
            else:
                node_tag_keys[e.attrib['k']] = 1
for nodes in node_tag_keys:
    #if the count of repetition is greater than 50 then it will print those names and their values
    if node_tag_keys[nodes] >= 50:
        print('{}->{}'.format(nodes,node_tag_keys[nodes]))
