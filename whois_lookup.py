import whois

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return {"error": str(e)}

# Example usage:
domain = "example.com"
print(whois_lookup(domain))
