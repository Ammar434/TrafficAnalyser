import binascii


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
    quote_a = bytes.fromhex(message).decode("ASCII")
    quote = quote_a.replace(";", "\n- ")
    return quote
