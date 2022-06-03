# Date: 06/03/2022
# Parsing XML using python!

from lxml import etree as ET

stream = open('sample.xml', 'r')

xml = ET.parse(stream)

root = xml.getroot()

for person in root.findall('Person'):
    person_id = person.get('Id')
    first_name = person.find('FirstName').text
    last_name = person.find('LastName').text
    email_addr = person.find('Email').text
    print(f"Full Name: {first_name} {last_name}")
    print(f"Person's ID Number: {person_id}")
    print(f"E-mail Address: {email_addr}\n")
