from copy import deepcopy
from services.integer_convert import binary_to_ip_dotted

from utils.constants import combo_box_initial_ip_dst, combo_box_initial_ip_src, combo_box_initial_protocol


class PrinterMethod:
    def __init__(self, listeField=[], listeProtocol=[]) -> None:
        self.listeField = listeField
        self.listeProtocol = listeProtocol
        self.listeIp = []
        self.listeDecodedTrame = []
        self.displayList = []

    def clearAll(self):
        self.listeField = []
        self.listeProtocol = []
        self.listeIp = []
        self.displayList = []
        self.listeDecodedTrame = []

    def displayThroughCriteria(self, src_ip, dst_ip, protocolToFind):
        self.displayList = []

        for trame in self.listeDecodedTrame:
            # print(trame)
            if trame != None:
                srcIP = trame.find_value_of_field("srcIpAddress", 3)
                srcIP = binary_to_ip_dotted(srcIP)
                dstIP = trame.find_value_of_field("dstIpAddress", 3)
                dstIP = binary_to_ip_dotted(dstIP)

                if (srcIP == src_ip or src_ip == combo_box_initial_ip_src):

                    if (dstIP == dst_ip or dst_ip == combo_box_initial_ip_dst):
                        if protocolToFind == "Http" or protocolToFind == combo_box_initial_protocol:
                            if trame.all_protocol_inside[7] != None:
                                if trame not in self.displayList:
                                    self.displayList.append(trame)
                        if protocolToFind == "Tcp" or protocolToFind == combo_box_initial_protocol:
                            if trame.all_protocol_inside[4] != None:
                                if trame not in self.displayList:
                                    self.displayList.append(trame)

                        if protocolToFind == "Ipv4" or protocolToFind == combo_box_initial_protocol:
                            if trame.all_protocol_inside[3] != None:
                                if trame not in self.displayList:
                                    self.displayList.append(trame)

                        if protocolToFind == "Ethernet" or protocolToFind == combo_box_initial_protocol:
                            if trame.all_protocol_inside[2] != None:
                                if trame not in self.displayList:
                                    self.displayList.append(trame)
