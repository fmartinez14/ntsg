import xml.etree.ElementTree as ET
from Packet import Packet
from Protocol import Protocol
from Field import Field
from pprint import pprint

def parsePDML():

    myFile = open("projectPCAP.pdml", 'r')

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

def makePackets():

    myFile = open("projectPCAP.pdml", 'r')

    # create element tree object
    tree = ET.parse(myFile)

    # get root element
    root = tree.getroot()

    # create empty list for objects
    Packets = {}

    for item in root.findall('packet'):
        TemporaryPacket = Packet(item.attrib)
        Packets[TemporaryPacket] = None
        Protocols = {}
        for child in item:
            # Packets[item] = child

            TemporaryProtocol = Protocol(child.attrib)
            FieldValues = []
            for fields in child.findall('field'):
                FieldValues.append(Field(fields.attrib))
            Protocols[TemporaryProtocol] = FieldValues
        Packets[TemporaryPacket] = Protocols


    ListMe = [Packets,Protocols]
    return ListMe

def printPackets(Packets,Protocols):
    for key,value in Packets.iteritems():
        print("----Protocol: \n")
        # print(str(type(Protocols[value])) + " Haaa")
        for key,fields in value.iteritems():
            print("                         Fields:")
            for myField in fields:
                print(myField.name)

def printTree(leTree):
    for item in tester:
        print("-------Packet\n")
        for protocol in item:
            print("-------------Protocol" + str(protocol.attrib) + "\n")
            for field in protocol:
                print("------------Field:" + str(field.attrib))
            print("\n")


# tester = parsePDML()
tester = makePackets()
printPackets(tester[0],tester[1])
# printTree(tester)
