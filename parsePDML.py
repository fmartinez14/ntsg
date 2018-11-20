import xml.etree.ElementTree as ET

def parsePDML():

    myFile = open("ipv4_cipso_option.pdml", 'r')

    # create element tree object
    tree = ET.parse(myFile)

    # get root element
    root = tree.getroot()
    
    # create empty list for objects
    Packets = {}
    Protocols = {}


    for item in root.findall('packet'):
        for child in item:
            Packets[item] = child
            FieldValues = []
            for fields in child.findall('field'):
                FieldValues.append(fields)
            Protocols[child] = FieldValues

    return Packets

def printTree(leTree):
    for item in tester:
        print("-------Packet\n")
        for protocol in item:
            print("-------------Protocol" + str(protocol.attrib) + "\n")
            for field in protocol:
                print("------------Field:" + str(field.attrib))
            print("\n")


tester = parsePDML()
