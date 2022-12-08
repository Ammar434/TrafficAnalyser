from models.protocol import ALL_PROTOCOl, Protocol
from services.decode_trame import DecodeTrame
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

for trame in decode:
    print(trame)
    print('-------------------------------------------------------------------------------------------------------------------------')

# print(len(decode))
