from Dependency import Dependency
from PDML import filterField

class Packet_Length_Dependency (Dependency):

	def __init__(self, packetName, fieldName):
		Dependency.__init__(self, PacketName, fieldName)

		rootPacket = PDML.filterField(PacketName)
		childField = PDML.filterField(fieldName)

		# satisfies SRS#97
		if rootPacket.getSize() < childField.getSize():
			raise Exception("Packet size not large enough for field")

		else:
			return self