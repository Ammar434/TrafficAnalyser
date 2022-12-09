from copy import deepcopy
from services.integer_convert import binary_to_hex, hex_to_ascii


list_of_trame = []


class Trame:

    def __init__(self, number, initialData) -> None:
        self.number = number
        self.data = initialData
        self.all_protocol_inside = {
            2: None,
            3: None,
            4: None,
            7: None,
        }

    def __str__(self) -> str:
        message = ""
        for key, protocol in self.all_protocol_inside.items():
            if protocol != None:
                if key == 7:
                    for l in protocol.fields:
                        print(l.content)
                        message = message + l.name + ' ' + \
                            hex_to_ascii(l.content) + '\n'
                else:
                    for field in protocol.fields:
                        message = message + ' '+field.name + \
                            ' ' + binary_to_hex(field.content) + '\n'

                message = message + '\n'
        return message

    def updateData(self, data):
        self.data = []
        self.data[:0] = data
        # print(len(self.data))

    def updateProtocolInside(self, layer, protocol):
        self.all_protocol_inside[layer] = deepcopy(protocol)

    def printListTrames(self, listTrames) -> str:
        for trame in listTrames:
            print(trame)

    def find_value_of_field(self, fieldId, layer):
        protocol = self.all_protocol_inside[layer]
        if protocol != None:
            for field in protocol.fields:
                # print(field.name + (field.content))
                # print(binary_to_hex(field.content))
                if field.id == fieldId:
                    return field.content

        return "Error"
