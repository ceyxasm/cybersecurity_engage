from scapy.all import *
ports= [25, 80, 53, 443, 445, 8080, 8443, 21, 22, 110, 995, 143, 993, 26, 587, 3306, 
            2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078] #not exhaustive

def synScan(host):
    ans, unans= sr( IP(dst= host)/TCP(sport=5555, dport= ports, flags="S"), timeout=2, verbose=0)
    print('open ports at %s' %host)
    for (s, r) in ans:
        if s[TCP].dport== r[TCP].sport:
            print(r[TCP].sport, ' ')

def DNSScan( host):
    ans, unans= sr( IP(dst= host)/UDP(sport=5555, dport= 53)/DNS(rd=1, qd=DNSQR(qname="google.com")), timeout=2, verbose=0)
    if ans:
        print("DNS server at %s"%host)

# host='8.8.8.8'
host= '14.139.37.109' #gateway of iitj
# host= '8.8.4.4'
synScan(host)
DNSScan(host)

'''
OPEN TECHNICAL DATABASES
________________________
1. https://who.is/
2. DNS
3. CDN
'''