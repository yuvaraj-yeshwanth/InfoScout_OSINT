import requests

def cms_detection(url):
    known_cms = {
        "WordPress": ["wp-content", "wp-includes"],
        "Joomla": ["Joomla!", "com_content"],
        "Drupal": ["drupal.js", "sites/all"],
        "Magento": ["mage/cookies.js", "Magento"]
    }

    try:
        response = requests.get(url)
        content = response.text
        headers = response.headers

        for cms, indicators in known_cms.items():
            for indicator in indicators:
                if indicator in content or indicator in headers.get("X-Powered-By", ""):
                    return f"{cms} CMS Detected"
        
        return "CMS not detected"
    except requests.RequestException as e:
        return f"Error: {str(e)}"

print(cms_detection("http://example.com"))
