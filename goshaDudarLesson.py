#!/usr/bin/env python3
import telebot
from random import randint
import xml.etree.ElementTree as ET
ALLSTRING_CONSTANT = 31102 #quantity of all strings

xml_data = open("data/biblrus.xml", 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML, при принте выводит <Element 'XMLBIBLE' at 0x7f1944625b80>
# data = []
# cols = []
# for i, child in enumerate(root):
#     data.append([subchild.text for subchild in child])
#     cols.append(child.tag)
# df = pd.DataFrame(data).T  # Write in DF and transpose it
# df.columns = cols  # Update column names

#print(root) #это корневой элемент
sentence = 'Привет, семейка!'

bot = telebot. TeleBot('6839894064:AAEPq1qi46vGNMyM3OEY-6kVkksGJT2MDaE')
@bot. message_handler(commands=['start'])
def main (message):
    randomString = randint(0, ALLSTRING_CONSTANT)#это последнее вставил
    stringNumber = 0
    for elem in root.iter():
    #print(elem.tag, elem.attrib, elem.text)
        if stringNumber == randomString:
            sentence = elem.text
        stringNumber+=1
    bot. send_message (message.chat.id,sentence)
bot.polling(none_stop=True) #polling translate as опрос