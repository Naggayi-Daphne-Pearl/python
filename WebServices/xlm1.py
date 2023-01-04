import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>1</id>
            <name>John Doe</name>
        </user>
         <user x="3">
            <id>1</id>
            <name>Joseph Doe</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    #  The text attribute of the name and id elements is used to get the text content of these elements. The text and get() methods return strings, which are printed to the console.
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    #get() gets the attribute value 
    print('Attribute:', item.get('x'))
