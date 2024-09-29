from urllib.parse import urlparse

def extract_domain_with_protocol(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    domain_with_protocol = f"{parsed_url.scheme}://{domain}"
    return domain_with_protocol

# Example usage:
url = "https://jarverse.blogspot.in/somw/owrwep"
domain = extract_domain_with_protocol(url)
print(domain)  # Output: www.example.com
