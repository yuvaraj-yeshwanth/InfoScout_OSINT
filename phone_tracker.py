import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_phone(phone_number):
    """
    Tracks phone number details including region, carrier, and timezone.

    Args:
        phone_number (str): The phone number to track (include country code, e.g., +1 or +91).
    
    Returns:
        dict: Details about the phone number.
    """
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid phone number"}
        
        # Get details
        region = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        # Return the results as a dictionary
        return {
            "Phone Number": formatted_number,
            "Region": region,
            "Carrier": carrier_name,
            "Timezones": list(timezones)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Test the phone tracker
    print("Welcome to the Phone Tracker!")
    print("Please ensure to provide the phone number with the country code (e.g., +1 for USA or +91 for India).")
    
    test_number = input("Enter the phone number: ").strip()
    result = track_phone(test_number)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\nPhone Number Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
