#-*- coding: utf-8 -*-
__author__ = "coolfire"

from scapy.all import *

def modify_packet_header(pkt):
	"""Parse the header and add an extra header"""
	if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
		hdr = pkt[TCP].payload.__dict__
		extra_item = {'Extra_Header' : ' extra value'}
		hdr.update(extra_item)
		send_hdr = '\r\n'.join(hdr)
		pkt[TCP].payload = send_hdr
		pkt.show()

		del pkt[IP].chksum
		send(pkt)

if __name__ == "__main__"
	#start sniffing
	sniff(filter="tcp and (port 80",prn=modify_packet_header)
