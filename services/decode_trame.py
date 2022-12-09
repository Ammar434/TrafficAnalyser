from models.field import Field
from models.protocol import ALL_PROTOCOl, Protocol
from models.trame import Trame
from services.integer_convert import binary_to_hex, hex_to_ascii, hex_to_bin
from copy import deepcopy, copy


class DecodeTrame:

    def identifyNextProtocol(self, protocol, trameField):

        if trameField != None:
            for field2 in trameField:

                for field in protocol.nextProtocolEncapsulated:
                    # print(field, field2.content)
                    if field2.id == field:
                        # print(field2.content)
                        return field2.content
        return ""

    def findNextProtocol(self, currentLayer, nextProtocol, trame):
        hexData = binary_to_hex(trame.data)

        # CODE FOR HTTP
        if currentLayer == 4 and ("48545450" in hexData or "68747470" in hexData):
            return ALL_PROTOCOl[7][0], 7

        for layer, listeProtocolForALayer in ALL_PROTOCOl.items():
            for protocol in listeProtocolForALayer:
                if protocol.protocolIdentification == nextProtocol:
                    return protocol, layer

        return None, ""

    def decodeOneField(self, field, trame, offset):
        minSize = field.minValue
        maxSize = field.maxValue
        cache = ""
        bitIndex = 0

        while (bitIndex < minSize or bitIndex < maxSize) and (bitIndex + offset) < len(
            trame
        ):

            cache = cache + trame[bitIndex + offset]

            bitIndex = bitIndex + 1

        # print(msgToPrint)
        return (cache, bitIndex)

    def decodeOptions(self, protocol, listFields, trame, offset):
        val = protocol.options.valueToBeGreather
        id = protocol.options.greatherThanField
        dif = 0
        message = ""

        for f in listFields:
            if f.id == id:
                # WE MULTIPLY BY 4 BECAUSE HEADER LENGTH REPRESENT THE LEN OF WORD
                dif = (int(f.content, 2) - val) * 4
                break

        i = 0
        while i < dif * 8:
            message = message + trame[i+offset]
            i = i + 1
        return (message, i)

    def decodeOneProtocol(self, protocolModel, trame):
        listFields = []
        offset = 0
        msgToPrint = ""
        for field in protocolModel.fields:
            newField = Field(field.id, field.name,
                             field.minValue, field.maxValue)

            # Chech if options is here
            message = ""
            index = 0
            msgToPrint = msgToPrint + " " + field.name + ": "

            # OPTION ARE TREATED IN ANOTHER FUNCTION
            if field.id == "options":
                message, index = self.decodeOptions(
                    protocolModel, listFields, trame, offset
                )
                newField.content = message

            else:
                message, index = self.decodeOneField(field, trame, offset)
                newField.content = message

            listFields.append(newField)
            offset = offset + index

            msgToPrint = msgToPrint + message + "\n"

        return listFields

    def decodeLayer7Protocol(self, protocolModel, trame):
        listFields = []
        listWithHeaderSeparated = []

        hexadecimalTrame = binary_to_hex(trame)
        headerAndBodyList = hexadecimalTrame.split(
            protocolModel.requestTypeSeparator + protocolModel.requestTypeSeparator)

        lineRequests = headerAndBodyList[0].split(
            protocolModel.requestTypeSeparator)

        for r in lineRequests:
            listWithHeaderSeparated.append(
                r.split(protocolModel.headerSeparator))

        listFields.append(Field("methode", "Request Methode",
                                content=listWithHeaderSeparated[0][0]))
        listFields.append(Field("requestUrl", "Request URI",
                                content=listWithHeaderSeparated[0][1]))

        listFields.append(Field("requestVersion", "Request Version",
                                content=listWithHeaderSeparated[0][2]))

        # print(listWithHeaderSeparated)
        for l in listWithHeaderSeparated[1:]:
            content = ""
            for c in l[1:]:
                content = content + ' ' + c

            listFields.append(Field(l[0], hex_to_ascii(l[0]), content=content))

        listFields.append(Field("body", "Corps de la requete",
                          content=headerAndBodyList[1]))
        return listFields

    def decodeAllProtocol(self, trameContent, count):
        currentProtocol = None
        currentProtocolLayer = None
        fields = None
        nextProtocol = "802.3"

        trame = Trame(count, trameContent)

        while nextProtocol != "":
            fields = []
            # print("nextProtoco " + nextProtocol)
            # FIRST STEP NEED TO FIND THE PROTOCOL IN THE DICT
            # BY THE END OF THIS LOOP WE KNOW THE NEXT PROOTCOL TO TREAT

            currentProtocol, currentProtocolLayer = self.findNextProtocol(
                currentProtocolLayer, nextProtocol, trame)

            # HTTP is decode differently

            if currentProtocol != None:
                if currentProtocolLayer == 7:
                    fields = self.decodeLayer7Protocol(
                        currentProtocol, trame.data)
                    trame.updateData('')
                else:
                    fields = self.decodeOneProtocol(
                        currentProtocol, trame.data)

                    for f in fields:
                        # print(f.name, print_binary_to_hex(f.content))
                        if f.id == "data":
                            trame.updateData(f.content)
                            break

                copyProtocol = deepcopy(currentProtocol)
                copyProtocol.fields = fields
                trame.updateProtocolInside(currentProtocolLayer, copyProtocol)

            nextProtocol = self.identifyNextProtocol(currentProtocol, fields)

            if nextProtocol == "Error":
                print("Error to find next protocol")
                return

            nextProtocol = binary_to_hex(nextProtocol)

        return trame

    def decodeAllTrame(self, listTrame):
        listDecodedTrame = []
        for count, trame in enumerate(listTrame):
            t = self.decodeAllProtocol(trame, count)
            listDecodedTrame.append(t)
        return listDecodedTrame
