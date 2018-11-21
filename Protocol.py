class Protocol:
    def __init__(self,data):
        for attribute in data:
            setattr(self, attribute, data[attribute])
        # self.Fields = data[0]
        # self.ProtocolFieldName = data[1]
        # self.ProtocolShowName = data[2]
        # self.ProtocolSize = data[3]
        # self.ProtocolPosition = data[4]
        # self.ProtocolShow = data[5]
        # self.ProtocolValue= data[6]
