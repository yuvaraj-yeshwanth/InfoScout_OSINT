from ipwhois import IPWhois

def reverse_ip_lookup(ip):
    ipwhois = IPWhois(ip)
    result = ipwhois.lookup_rdap()
    return result

# Example usage:
ip = "8.8.8.8"
print(reverse_ip_lookup(ip))
