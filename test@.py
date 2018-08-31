import os
import sys
sys.path.append("/home/ezpedvi/myimports/")
import dpkt
import datetime

timestamps = []
mtu = []

count_tipc = 0
count_ipv6 = 0
count_ipv4 = 0
count_tcp = 0
count_udp = 0
count_icmp = 0
count_icmp_ipv6 = 0
count_sctp = 0


for filename in os.listdir('/home/ezpedvi/packets_oneHour_mtas-35-2_INM_Ipv6_mtu_2140_case2_20180823'):
        if filename.startswith('packetinfo'):
                print filename
                with open(os.path.join('/home/ezpedvi/packets_oneHour_mtas-35-2_INM_Ipv6_mtu_2140_case2_20180823', filename)) as f:
                        pcap = dpkt.pcap.Reader(f)
                        try:
                                for timestamp, buf in pcap:
                                        eth = dpkt.ethernet.Ethernet(str(buf))

                                        if eth.type == 35018:
                                                count_tipc += 1
                                        else:
                                                ip = eth.data
                                                ip2=eth.data
                                                if ip.p == 41 or ip2.p == 41:
                                                        count_ipv6 += 1
                                                elif ip.p == 4 or ip2.p == 4:
                                                        count_ipv4 += 1
                                                elif ip.p == 6 or ip2.p == 6:
                                                        count_tcp += 1
                                                elif ip.p == 17 or ip2.p == 17:
                                                        count_udp += 1
                                                elif ip.p == 58 or ip2.p == 58:
                                                        count_icmp_ipv6 += 1
                                                elif ip.p == 1 or ip2.p == 1:
                                                        count_icmp += 1
                                                elif ip.p == 132 or ip2.p == 132:
                                                        count_sctp += 1
                        except AttributeError:
                                pass
                        print "count_tipc =%s, count_icmp_impv6=%s, count_icmp=%s, count_udp=%s, count_tcp=%s, count_sctp=%s, count_ipv6=%s, count_ipv4=%s"%(count_tipc, count_icmp_ipv6, count_icmp, count_udp, count_tcp, count_sctp, count_ipv6, count_ipv4)
                        print count_icmp_ipv6 + count_icmp + count_tcp + count_udp + count_sctp + count_ipv4 + count_ipv6 + count_tipc
