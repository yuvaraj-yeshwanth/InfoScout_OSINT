
from modules.webosint import cms_detection, nslookup, reverse_ip, subdomain_enum, whois_lookup

def main():
    print("\nInfoScout: WebOSINT\n")
    print("1. CMS Detection\n2. NSLookup\n3. Reverse IP Lookup\n4. Subdomain Enumeration\n5. Whois Lookup\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        cms_detection.detect_cms()
    elif choice == 2:
        nslookup.perform_nslookup()
    elif choice == 3:
        reverse_ip.lookup_reverse_ip()
    elif choice == 4:
        subdomain_enum.enumerate_subdomains()
    elif choice == 5:
        whois_lookup.perform_whois()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
