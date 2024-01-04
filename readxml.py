#import io
import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open("data/biblrus.xml", 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(root.find('ак совершены небо и земля и все воинство '))

#bible = pd.read_csv("data/biblrus.xml")
#print(bible)