import dns.resolver

def nslookup(domain):
    result = {}
    try:
        result["A"] = dns.resolver.resolve(domain, "A")
        result["MX"] = dns.resolver.resolve(domain, "MX")
        result["NS"] = dns.resolver.resolve(domain, "NS")
        result["TXT"] = dns.resolver.resolve(domain, "TXT")
        result["CNAME"] = dns.resolver.resolve(domain, "CNAME")
    except Exception as e:
        return {"error": str(e)}

    return result

print(nslookup("example.com"))
