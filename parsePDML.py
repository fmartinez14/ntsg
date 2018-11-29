import xml.etree.ElementTree as ET
from Packet import Packet
from Protocol import Protocol
from Field import Field


def parsePDML(): #Dont use me , parses pdml but does not create objects inside the packets.
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

def printTree(leTree): #Dont use me, used for debugging the extraction and creation w/o objects.
    for item in tester:
        print("-------Packet\n")
        for protocol in item:
            print("-------------Protocol" + str(protocol.attrib) + "\n")
            for field in protocol:
                print("------------Field:" + str(field.attrib))
            print("\n")


def makePackets(fileName): #Creates a Packet Dictionary object, where the keys are Packet objects and the values are Protocol objects. Furthermore, the Protocol Dictionary that is also returned contains the protocols as keys and a list of fields as a value.
    myFile = open(fileName, 'r')

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



def printPackets(Packets,Protocols): #Prints the resulting packet/protocol/field name.
    for key,value in Packets.iteritems():
        print("----Protocol: \n")
        # print(str(type(Protocols[value])) + " Haaa")
        for key,fields in value.iteritems():
            print("                         Fields:")
            for myField in fields:
                print(myField.name)


if __name__ == '__main__':
    # tester = parsePDML()
    tester = makePackets()
    printPackets(tester[0],tester[1])
    # printTree(tester)
