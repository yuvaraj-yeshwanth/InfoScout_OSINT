import re
import dns.resolver

def email_scanner(text):
    """
    Extracts and validates email addresses from a given text.
    :param text: String containing the text to scan.
    :return: Dictionary with valid and invalid email addresses.
    """
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_regex, text)
    valid_emails = []
    invalid_emails = []

    for email in emails:
        if validate_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    return {"valid_emails": valid_emails, "invalid_emails": invalid_emails}

def validate_email(email):
    """
    Validates an email address by checking its domain's MX records.
    :param email: The email address to validate.
    :return: True if the email is valid, False otherwise.
    """
    try:
        domain = email.split('@')[-1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return False
    except Exception as e:
        print(f"Error validating {email}: {e}")
        return False

# Example usage
if __name__ == "__main__":
    sample_text = """
    Here are some emails to check: 
    - valid.email@example.com
    - invalid.email@nonexistentdomain.xyz
    - another.valid+email@gmail.com
    """
    results = email_scanner(sample_text)
    print("Valid Emails:", results["valid_emails"])
    print("Invalid Emails:", results["invalid_emails"])
