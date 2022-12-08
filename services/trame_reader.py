from services.integer_convert import hex_to_bin, is_hex


# USE TO READ TRAME
class TrameReader:
    rawText = ""
    rawTrame = []
    rawAllTrame = []
    allTrameLinear = []

    def createTramesList(self, tramePath):
        self.readFromTxt(tramePath)
        self.extractAllTrame()
        self.arrangeAllTrame()
        return self.allTrameLinear

    def readFromTxt(self, tramePath):
        try:
            with open(tramePath) as f:
                for line in f:
                    self.rawText = self.rawText + line
            self.rawTrame = self.rawText.replace("\n", " ").replace("\r", "")
            self.rawTrame = self.rawTrame.split(" ")

        except FileNotFoundError:
            print("That file was not found")

    def extractAllTrame(self):
        i = 0
        while i < (len(self.rawTrame)):
            trame = []
            # Beginning of trame
            if self.rawTrame[i] == "0000":
                trame.append(self.rawTrame[i])
                i = i + 1
                while i < (len(self.rawTrame)):
                    if self.rawTrame[i] == "0000":
                        break
                    trame.append(self.rawTrame[i])
                    i += 1
                self.rawAllTrame.append(trame)
                i = i - 1
            i = i + 1

    def arrangeAllTrame(self):

        for trame in self.rawAllTrame:
            t = self.arrangeTrame(trame)
            self.allTrameLinear.append(t)

    def arrangeTrame(self, l):
        listeOfBytes = [s for s in l if len(s) == 2 and is_hex(s) == True]

        listeOfHex = []
        listeOfBits = []
        for l in listeOfBytes:
            listeOfHex.extend(l)
        for l in listeOfHex:
            listeOfBits.extend(hex_to_bin(l))
        listeOffset = [s for s in l if len(s) == 4]

        return listeOfBits

    def checkErrorAndPadding():
        # trame start wirh 0000

        # len of trame is equal to last offset + 16

        pass
