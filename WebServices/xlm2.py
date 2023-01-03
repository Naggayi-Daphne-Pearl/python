import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET MODUE 
tree = ET.parse('./holders.xml')
root = tree.getroot()
print(ET.tostring(root))