class Packet:
    def __init__(self,data):
        for attribute in data:
            setattr(self, attribute, data[attribute])

        # self.protocols = data[0]
        # self.PacketName = data[1]
        # self.PacketSize = data[2]
