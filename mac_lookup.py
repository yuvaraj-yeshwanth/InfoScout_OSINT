import requests

def mac_lookup(mac_address):
    """
    Looks up a MAC address using an online API.
    :param mac_address: The MAC address to look up.
    :return: Vendor information or error message.
    """
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Vendor: {response.text}"
        else:
            return f"Error: Unable to fetch details for {mac_address}."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    mac = input("Enter MAC address: ")
    print(mac_lookup(mac))
