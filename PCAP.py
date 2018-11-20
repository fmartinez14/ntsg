from subprocess import call

class PCap:
    def __init__(self,PCAPLocation):
        self.fileLocation = PCAPLocation

    def convertPCAP(self):
        fileName = self.obtainFileName()
        print "Converting"
        print("Arguments: tshark -r "+ self.fileLocation + " -T pdml > " + fileName)
        call("tshark -r "+ self.fileLocation + " -T pdml > " + fileName,shell=True)
        print "Done"

    def obtainFileName(self):
        filePath = self.fileLocation.split("/")
        fileName = filePath[-1]
        fileExt = fileName.split(".")
        return fileExt[0] + ".pdml"
