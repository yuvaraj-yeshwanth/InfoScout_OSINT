import scapy.all as scapy

def port_scanner(target):
    open_ports = []
    for port in range(1, 1025):
        # Send SYN packets
        syn = scapy.IP(dst=target)/scapy.TCP(dport=port, flags="S")
        response = scapy.sr1(syn, timeout=1, verbose=False)

        # Check if SYN-ACK response (open port)
        if response and response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 18:
            open_ports.append(port)

    return open_ports

# Example usage:
host = "192.168.1.1"
print(port_scanner(host))
