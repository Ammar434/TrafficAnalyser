# class PrintForDebug:
#     def printTrame(self):


def print_binary_list_to_hex(trame):
    decodeMsg = ""
    cache = ""

    for bit in trame:
        cache = cache + bit
        if len(cache) == 4 and cache != "":
            toAdd = "%X" % int(cache, 2)
            decodeMsg = decodeMsg + toAdd
            cache = ""
    print(decodeMsg)
