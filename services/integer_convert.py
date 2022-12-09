import binascii
import ipaddress
from qt_core import QColor


from models.protocol import ALL_PROTOCOl


def is_hex(s):
    for ch in s:
        if (ch < "0" or ch > "9") and (ch < "A" or ch > "F") and (ch < "a" or ch > "f"):
            return False
    return True


def hex_to_bin(hexval):
    """
    Takes a string representation of hex data with
    arbitrary length and converts to string representation
    of binary.  Includes padding 0s
    """
    thelen = len(hexval) * 4
    binval = bin(int(hexval, 16))[2:]
    while (len(binval)) < thelen:
        binval = "0" + binval
    return binval


def binary_to_hex(trame):
    bitIndex = 0
    decodeMsg = ""
    cache = ""
    while bitIndex < len(trame):

        cache = cache + trame[bitIndex]

        # Only for display purpose
        if len(cache) == 4 and cache != "":
            toAdd = "%X" % int(cache, 2)

            decodeMsg = decodeMsg + toAdd
            cache = ""

        bitIndex = bitIndex + 1
    # print(decodeMsg)
    if decodeMsg == "":
        return cache
    return decodeMsg


def hex_to_ascii(message):
    try:
        quote_a = bytes.fromhex(message).decode("ASCII")
        quote = quote_a.replace(";", "\n- ")
        return quote
    except ValueError:
        return "-1"


def binary_to_ip_dotted(message):
    decodeMsg = ""
    cache = ""
    for m in message:
        cache = cache + m
        if len(cache) == 8 and cache != "":
            toAdd = int(cache, 2)
            decodeMsg = decodeMsg + str(toAdd) + '.'
            cache = ""
    return decodeMsg[:-1]


def binary_to_mac_dotted(message):
    decodeMsg = ""
    cache = ""
    for m in message:
        cache = cache + m
        if len(cache) == 8 and cache != "":
            toAdd = int(cache, 2)
            decodeMsg = decodeMsg + str(toAdd) + '.'
            cache = ""
    return decodeMsg[:-1]


def add_flags(trame):
    message = ""
    val = trame.find_value_of_field("ecn-accurate", 4)
    if val != "Error" and val != "0":
        message = message + "ECN "

    val = trame.find_value_of_field("cwr", 4)
    if val != "Error" and val != "0":
        message = message + "CWR "

    val = trame.find_value_of_field("ecn-echo", 4)
    if val != "Error" and val != "0":
        message = message + "ECN ECHO "

    val = trame.find_value_of_field("urgent", 4)
    if val != "Error" and val != "0":
        message = message + "URG "

    val = trame.find_value_of_field("ack", 4)
    if val != "Error" and val != "0":
        message = message + "ACK "

    val = trame.find_value_of_field("psh", 4)
    if val != "Error" and val != "0":
        message = message + "PUSH "

    val = trame.find_value_of_field("rst", 4)
    if val != "Error" and val != "0":
        message = message + "RST "

    val = trame.find_value_of_field("syn", 4)
    if val != "Error" and val != "0":
        message = message + "SYN "

    val = trame.find_value_of_field("fin", 4)
    if val != "Error" and val != "0":
        message = message + "FIN "

    return message[:-1]


def message_for_row_ethernet(trame):
    message = ""
    message_1 = ""

    message_1 = message_1 + "Protocole Encapsule : "
    val = trame.find_value_of_field("nextProtocolNumber", 2)

    if val != "Error":
        message_1 = message_1 + binary_to_hex(val)
    else:
        message_1 = message_1 + val

   # MAC SRC
    val = trame.find_value_of_field("sourceMacAddress", 2)

    if val != "Error":
        message = message + binary_to_mac_dotted(val)
    else:
        message = message + val

    message = message + " " + printArrow(120 - len(message)) + " "
    # MAC DST

    val = trame.find_value_of_field("destMacAddress", 2)
    if val != "Error":
        message = message + binary_to_mac_dotted(val)
    else:
        message = message + val

    # message = message.center(250 - len(message))
    m = message_1+'\n' + message
    return m


def printArrow(num):
    msg = ""
    n = 0
    while n < num - 1:
        msg = msg + '-'
        n = n + 1
    msg = msg + ">"
    return msg


def message_for_row_ipv4(trame):
    message = ""
    message_1 = ""

    message_1 = message_1 + "Protocole Encapsule : "
    val = trame.find_value_of_field("nextProtocolNumber", 3)

    # print(trame)
    # print(val)
    if val != "Error":
        message_1 = message_1 + binary_to_hex(val)
    else:
        message_1 = message_1 + val

    # message_1 = message_1.center(250 - len(message_1))
    # MAC SRC

    val = trame.find_value_of_field("srcIpAddress", 3)

    if val != "Error":
        message = message + binary_to_ip_dotted(val)
    else:
        message = message + val

    # MAC DST
    message = message + " " + printArrow(120 - len(message)) + " "

    val = trame.find_value_of_field("dstIpAddress", 3)
    if val != "Error":
        message = message + binary_to_ip_dotted(val)
    else:
        message = message + val
    # print('azref')
    # print(message)
    # message = message.center(250 - len(message))
    m = message_1+'\n' + message
    return m


def message_for_row_tcp(trame):

    message = ""
    message_1 = ""

    # Flag tcp SYN ACK PSH ...
    message = message + ' ['
    message = message + add_flags(trame)
    message = message + ']'

    # Seqence num
    val = trame.find_value_of_field("sequenceNumber", 4)
    message = message + " SN="
    if val != "Error":
        hexValue = binary_to_hex(val)
        while hexValue[0] == '0':
            hexValue = hexValue[1:]
        message = message + hexValue
    else:
        message = message + " "+val

    # Ack num
    val = trame.find_value_of_field("acknowledgement", 4)
    message = message + " ACK="
    if val != "Error":
        hexValue = binary_to_hex(val)
        while hexValue[0] == '0' and len(hexValue) > 1:
            hexValue = hexValue[1:]
        message = message + hexValue
    else:
        message = message + val

    # Window
    val = trame.find_value_of_field("windows", 4)
    message = message + " WND="

    if val != "Error":
        message = message + str(int(val, 2))
    else:
        message = message + val

    val = trame.find_value_of_field("ttl", 3)
    message = message + " TTL="

    if val != "Error":
        message = message + str(int(val, 2))
    else:
        message = message + val

    val = trame.find_value_of_field("srcIpAddress", 3)
    if val != "Error":
        message_1 = message_1 + binary_to_ip_dotted(val)+"::"
    else:
        message_1 = message_1 + val+":"

    # Port source
    val = trame.find_value_of_field("portSource", 4)
    if val != "Error":
        message_1 = message_1 + str(int(val, 2))
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ' ('

    # MAC SRC
    val = trame.find_value_of_field("sourceMacAddress", 2)

    if val != "Error":
        message_1 = message_1 + "MAC "+binary_to_mac_dotted(val)
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ") " + printArrow(120 - len(message_1)) + " "

    val = trame.find_value_of_field("dstIpAddress", 3)
    if val != "Error":
        message_1 = message_1 + binary_to_ip_dotted(val)+"::"
    else:
        message_1 = message_1 + val+":"
    # Port dest
    val = trame.find_value_of_field("portDestination", 4)
    message_1 = message_1 + " " + str(int(val, 2))

    # MAC DST
    message_1 = message_1 + ' ('

    val = trame.find_value_of_field("destMacAddress", 2)
    if val != "Error":
        message_1 = message_1 + "MAC " + binary_to_mac_dotted(val)
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ')'

    m = message+'\n' + message_1

    return m


def message_for_row_http(trame):
    message = ""
    message_1 = ""
    # Type methode
    val = trame.find_value_of_field("methode", 7)
    message = message + hex_to_ascii(val) + " "

    # uri
    val = trame.find_value_of_field("requestUrl", 7)
    message = message + hex_to_ascii(val) + " "

    # version
    val = trame.find_value_of_field("requestVersion", 7)
    message = message + hex_to_ascii(val) + " "

    val = trame.find_value_of_field("srcIpAddress", 3)
    if val != "Error":
        message_1 = message_1 + binary_to_ip_dotted(val)+"::"
    else:
        message_1 = message_1 + val+":"

    # Port source
    val = trame.find_value_of_field("portSource", 4)
    if val != "Error":
        message_1 = message_1 + str(int(val, 2))
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ' ('

    # MAC SRC
    val = trame.find_value_of_field("sourceMacAddress", 2)

    if val != "Error":
        message_1 = message_1 + "MAC "+binary_to_mac_dotted(val)
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ") " + printArrow(120 - len(message_1)) + " "

    val = trame.find_value_of_field("dstIpAddress", 3)
    if val != "Error":
        message_1 = message_1 + binary_to_ip_dotted(val)+"::"
    else:
        message_1 = message_1 + val+":"
    # Port dest
    val = trame.find_value_of_field("portDestination", 4)
    message_1 = message_1 + " " + str(int(val, 2))

    # MAC DST
    message_1 = message_1 + ' ('

    val = trame.find_value_of_field("destMacAddress", 2)
    if val != "Error":
        message_1 = message_1 + "MAC " + binary_to_mac_dotted(val)
    else:
        message_1 = message_1 + val

    message_1 = message_1 + ')'
    m = message+'\n' + message_1

    return m


def message_for_row(trame):
    message = "Protocole non supporte"
    if trame.all_protocol_inside[7] != None:
        if trame.all_protocol_inside[7].name == "Http":
            tmp = message_for_row_http(trame)
            if tmp != None:
                return tmp, QColor(236, 64, 122)

    if trame.all_protocol_inside[4] != None:
        if trame.all_protocol_inside[4].name == "Tcp":
            tmp = message_for_row_tcp(trame)
            if tmp != None:
                return tmp, QColor(255, 138, 101)

    if trame.all_protocol_inside[3] != None:
        if trame.all_protocol_inside[3].name == "Ipv4":
            tmp = message_for_row_ipv4(trame)
            if tmp != None:
                return tmp,  QColor(224, 224, 224)

    if trame.all_protocol_inside[2] != None:
        if trame.all_protocol_inside[2].name == "Ethernet":
            tmp = message_for_row_ethernet(trame)
            if tmp != None:
                return tmp,  QColor(188, 170, 164)
    return message
