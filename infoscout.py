
import os
from modules.trackers import ip_tracker, phone_tracker, mac_lookup, email_scanner, metadata_extractor, reverse_image, port_scanner

def main():
    print("\nInfoScout: OSINT Tracker\n")
    print("1. IP Tracker\n2. Phone Number Tracker\n3. MAC Address Lookup\n4. Email Scanner\n5. Metadata Extractor\n6. Reverse Image Search\n7. Port Scanner\n")
    choice = int(input("Choose an option: "))

    if choice == 1:
        ip_tracker.track_ip()
    elif choice == 2:
        phone_tracker.track_phone()
    elif choice == 3:
        mac_lookup.lookup_mac()
    elif choice == 4:
        email_scanner.scan_email()
    elif choice == 5:
        metadata_extractor.extract_metadata()
    elif choice == 6:
        reverse_image.search_image()
    elif choice == 7:
        port_scanner.scan_ports()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
