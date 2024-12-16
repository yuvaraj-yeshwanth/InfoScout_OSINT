
# InfoScout

InfoScout is a Python-based OSINT tool for information gathering.

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
You are now ready to use InfoScout. If you are done, deactivate the virtual environment using:
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

## License
GPL-3.0 License
