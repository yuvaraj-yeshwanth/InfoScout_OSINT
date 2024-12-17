
import sys
from modules.trackers import (
    ip_tracker,
    phone_tracker,
    mac_lookup,
    email_scanner,
    metadata_extractor,
    reverse_image,
    port_scanner,
    cms_detection,
    nslookup,
    reverse_ip_lookup,
    subdomain_enumeration,
    whois_lookup
)

def main():
    print("Welcome to InfoScout OSINT Tool!")
    print("Select an OSINT tool to use:")
    print("1. IP Tracker")
    print("2. Phone Tracker")
    print("3. MAC Lookup")
    print("4. Email Scanner")
    print("5. Metadata Extractor")
    print("6. Reverse Image Search")
    print("7. Port Scanner")
    print("8. CMS Detection")
    print("9. NSLookup")
    print("10. Reverse IP Lookup")
    print("11. Subdomain Enumeration")
    print("12. Whois Lookup")
    print("13. Exit")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        ip_address = input("Enter the IP address to track: ")
        result = ip_tracker.track_ip(ip_address)
        print(result)
    elif choice == "2":
        phone_number = input("Enter the phone number with country code (e.g., +1 or +91): ")
        result = phone_tracker.track_phone(phone_number)
        print(result)
    elif choice == "3":
        mac_address = input("Enter the MAC address to lookup: ")
        result = mac_lookup.lookup_mac(mac_address)
        print(result)
    elif choice == "4":
        email = input("Enter the email address to scan: ")
        result = email_scanner.scan_email(email)
        print(result)
    elif choice == "5":
        file_path = input("Enter the file path of the media file (e.g., image, PDF) to extract metadata: ")
        result = metadata_extractor.extract_metadata(file_path)
        print(result)
    elif choice == "6":
        image_path = input("Enter the image path for reverse image search: ")
        api_key = input("Enter your Google API Key: ")
        cx = input("Enter your Custom Search Engine ID: ")
        result = reverse_image.reverse_image(image_path, api_key, cx)
        print(result)
    elif choice == "7":
        target_ip = input("Enter the IP address or domain to scan: ")
        result = port_scanner.scan_ports(target_ip)
        print(result)
    elif choice == "8":
        target_url = input("Enter the URL to detect CMS: ")
        result = cms_detection.detect_cms(target_url)
        print(result)
    elif choice == "9":
        domain = input("Enter the domain to perform NSLookup: ")
        result = nslookup.perform_nslookup(domain)
        print(result)
    elif choice == "10":
        ip_address = input("Enter the IP address to perform reverse IP lookup: ")
        result = reverse_ip_lookup.reverse_ip_lookup(ip_address)
        print(result)
    elif choice == "11":
        domain = input("Enter the domain to enumerate subdomains: ")
        result = subdomain_enumeration.enumerate_subdomains(domain)
        print(result)
    elif choice == "12":
        domain = input("Enter the domain to perform Whois lookup: ")
        result = whois_lookup.whois_lookup(domain)
        print(result)
    elif choice == "13":
        print("Exiting the tool.")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
