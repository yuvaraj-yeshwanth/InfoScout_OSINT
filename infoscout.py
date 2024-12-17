
import os
from modules.trackers import (
    ip_tracker,
    phone_tracker,
    mac_lookup,
    email_scanner,
    metadata_extractor,
    reverse_image,
    port_scanner
)

def main():
    print("\nInfoScout: OSINT Tracker\n")
    print("1. IP Tracker\n2. Phone Number Tracker\n3. MAC Address Lookup\n4. Email Scanner\n5. Metadata Extractor\n6. Reverse Image Search\n7. Port Scanner\n")
    
    try:
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            ip_address = input("Enter IP address to track: ")
            ip_tracker.track_ip(ip_address)
        elif choice == 2:
            phone_number = input("Enter phone number (with country code): ")
            phone_tracker.track_phone(phone_number)
        elif choice == 3:
            mac_address = input("Enter MAC address to lookup: ")
            mac_lookup.lookup_mac(mac_address)
        elif choice == 4:
            email = input("Enter email to scan: ")
            email_scanner.scan_email(email)
        elif choice == 5:
            file_path = input("Enter file path to extract metadata: ")
            metadata_extractor.extract_metadata(file_path)
        elif choice == 6:
            image_path = input("Enter image path for reverse image search: ")
            reverse_image.search_image(image_path)  # Pass the image path to the reverse image function
        elif choice == 7:
            target_ip = input("Enter IP address or domain for port scanning: ")
            port_scanner.scan_ports(target_ip)
        else:
            print("Invalid choice. Exiting.")
            
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
