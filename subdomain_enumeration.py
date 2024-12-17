from sublist3r import Sublist3r

def subdomain_enumeration(domain):
    sublist3r = Sublist3r.Sublist3r()
    subdomains = sublist3r.enumerate(domain)
    return subdomains

# Example usage:
domain = "example.com"
print(subdomain_enumeration(domain))
