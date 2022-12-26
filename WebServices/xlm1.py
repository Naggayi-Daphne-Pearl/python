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
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))
