#import io
from random import randint
import xml.etree.ElementTree as ET
import pandas as pd
ALLSTRING_CONSTANT = 31102

xml_data = open("data/biblrus.xml", 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML, при принте выводит <Element 'XMLBIBLE' at 0x7f1944625b80>

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
#print(df)
print(root) #это корневой элемент

randomString = randint(0, ALLSTRING_CONSTANT)
sentence = ''
#это работает, это напечатает тэги всех элементов, лучше не запускать
index_i=0
stringNumber = 0
for elem in root.iter():
    #print(elem.tag, elem.attrib, elem.text)
    if stringNumber == randomString:
        #for x in range (stringNumber, stringNumber+5):
         #   if elem.tag=='VERS':
        sentence = elem.text
        print(sentence)
    stringNumber+=1
    #index_i+=1
    #if index_i >=50:
     #   break
#print('совесных строк = ', stringNumber)  

#это работает, выведет атрибуты всех элементов с тегом BIBLEBOOK
##for elem in root.findall('BIBLEBOOK'):
##    print(elem.attrib)

#bible = pd.read_csv("data/biblrus.xml")
#print(bible)
