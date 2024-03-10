#!/usr/bin/python2.7

import sys
from pcapy import open_offline, open_live
from impacket.ImpactDecoder import EthDecoder

class ImpacketDemo(object):

    def __init__(self):
        super(ImpacketDemo, self).__init__()
        pass

    def read_packet(self, hdr, data):
        decoder = EthDecoder()
        ether = decoder.decode(data)
        ip = ether.child()
        tcp = ip.child()
        src_ip = ip.get_ip_src()
        src_port = tcp.get_th_sport()
        dst_ip = ip.get_ip_dst()
        dst_port = tcp.get_th_dport()
        try:
            print 'src_ip:src_port is %s:%s\n' % (src_ip,src_port)
            #print 'src_ip: %s\n' % src_ip
            #print 'src_port: %s\n' % src_port
            
            print 'dst_ip:dst_port is %s:%s\n' %(dst_ip,dst_port)
            #print 'dst_ip: %s\n' % dst_ip
            #print 'dst_port %s\n' % dst_port
        except:
            pass

    def main(self, pcap_file):
        pcap = open_offline(pcap_file)
        # this.read_packet
        pcap.loop(0, self.read_packet)

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        sys.exit("Usage: %s <filename>" % sys.argv[0])
    
    demo = ImpacketDemo()
    demo.main(sys.argv[1])