import xml.etree.ElementTree as ET

tree = ET.parse('Country_data.xml')
root = tree.getroot()

print('Printing All Attributes')
for elem in root:
    for subelem in elem:
        print(subelem.tag, ' - ', subelem.text)
        
#print(root[0][1].text)

#file = open('JournalEntries_OLF.xml','r')

#if file.mode == 'r':
    #contents = file.read()
    #print(contents)