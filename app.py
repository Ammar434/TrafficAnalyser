from models.protocol import ALL_PROTOCOl, Protocol
from services.decode_trame import DecodeTrame
from services.integer_convert import binary_to_ip_dotted
from services.trame_reader import TrameReader
from utils.constants import SUCCESS

res = Protocol.loadAllProtocol()

# print(len(ALL_PROTOCOl))

if res != SUCCESS:
    print("All protocol not load correctly")


trameReader = TrameReader()
listTrame = trameReader.createTramesList("trames/t.txt")

# trameReader.printListTrames(listTrame)

# decode = DecodeTrame().decodeOneProtocol(ALL_PROTOCOl[2][0], listTrame[0])
# print(decode)

# decode2 = DecodeTrame().decodeOneProtocol(ALL_PROTOCOl[3][0], decode)
# decode3 = DecodeTrame().decodeOneProtocol(ALL_PROTOCOl[4][0], decode2)
# decode4 = DecodeTrame().decodeLayer7Protocol(ALL_PROTOCOl[7][0], decode3)

# print(decode2)

decode = DecodeTrame().decodeAllTrame(listTrame)

# listeIp = []
for trame in decode:
    print(trame)
    print('-------------------------------------------------------------------------------------------------------------------------')


# for trame in decode:
#     if trame != None:
#         if trame.all_protocol_inside[3] != None:
#             print(len(trame.all_protocol_inside[3].fields))
#             print(trame)
#             print('-------------------------------------------------------------------------------------------------------------------------')

#             for field in trame.all_protocol_inside[3].fields:
#                 if field.id == "srcIpAddress" or field.id == "dstIpAddress":
#                     newIp = binary_to_ip_dotted(field.content)
#                     if newIp not in listeIp:
#                         listeIp.append(binary_to_ip_dotted(field.content))

# print(listeIp)
