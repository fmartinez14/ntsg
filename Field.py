class Field:
    def __init__(self,data):
        for attribute in data:
            setattr(self, attribute, data[attribute])
        # self.FieldName = data[0]
        # self.FieldShowName = data[1]
        # self.FieldPosition = data[2]
        # self.FieldSize = data[3]
        # self.FieldValue= data[4]
        # self.FieldShow = data[5]
