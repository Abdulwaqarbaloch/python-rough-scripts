from scapy.all import *



def sniffer(pkt):
    
    if pkt.haslayer(DNS) and pkt.haslayer(IP):
        
        source_ip = pkt[IP].src
        print("source ip: ", source_ip)
        






def main():
    sniff(prn=sniffer)

if __name__ == '__main__':
    main()