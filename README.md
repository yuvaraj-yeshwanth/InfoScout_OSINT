
# InfoScout

InfoScout is a Python-based OSINT (Open Source Intelligence) tool for information gathering.

## Features
- IP Tracker
- Phone Number Tracker
- MAC Address Lookup
- Email Scanner
- Metadata Extractor
- Reverse Image Search
- Port Scanner
- CMS Detection
- NSLookup
- Reverse IP Lookup
- Subdomain Enumeration
- Whois Lookup

## Installation

To avoid system-level Python restrictions, we recommend using a virtual environment to install dependencies.

### Step 1: Clone the Repository
```bash
git clone https://github.com/yuvaraj-yeshwanth/InfoScout_OSINT.git
cd InfoScout
```

### Step 2: Create and Activate a Virtual Environment
#### On Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Tool
You are now ready to use InfoScout. To start the tool:
```bash
python3 infoscout.py
```

When you are finished, deactivate the virtual environment using:
```bash
deactivate
```

## Usage
### OSINT Trackers
```bash
python3 infoscout.py
```

### WebOSINT
```bash
python3 webosint.py
```

## Modules and Dependencies

Each module of InfoScout relies on specific Python libraries. Below are the primary dependencies used:

1. **IP Tracker**: Uses `requests` and `ipinfo` APIs.
2. **Phone Number Tracker**: Requires the `phonenumbers` library:
   ```bash
   pip install phonenumbers
   ```
3. **MAC Address Lookup**: Depends on `getmac`.
4. **Email Scanner**: Utilizes `validate_email_address`.
5. **Metadata Extractor**: Leverages `pillow` and `exifread`.
6. **Reverse Image Search**: Supports Google Reverse Image Search API.
7. **Port Scanner**: Uses `socket`.
8. **CMS Detection**: Integrates with `whatweb`.
9. **NSLookup**: Relies on built-in Python DNS resolver libraries.
10. **Reverse IP Lookup**: Utilizes third-party OSINT APIs.
11. **Subdomain Enumeration**: Uses tools like `sublist3r`.
12. **Whois Lookup**: Requires `python-whois`.

## Contributing
Contributions to InfoScout are welcome! Feel free to fork the repository, submit pull requests, or suggest new features.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push the branch and open a pull request.

## License
InfoScout is licensed under the **GPL-3.0 License**, ensuring it remains free and open source.

---

If you encounter any issues or have suggestions, please feel free to open an issue or contact us.

Happy tracking!
