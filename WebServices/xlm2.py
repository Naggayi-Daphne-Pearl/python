import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET MODUE 
tree = ET.parse('holders.xml')
root = tree.getroot()

# Get attribute 
coin = root.get('coin')
print('Crypto name: {val}'. format(val=coin))