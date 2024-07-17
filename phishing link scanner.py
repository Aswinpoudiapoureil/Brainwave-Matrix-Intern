import tldextract
import Levenshtein as lv

legitimate_domains = [
    'example.com', 'google.com', 'facebook.com', 'amazon.com', 'apple.com',
    'microsoft.com', 'netflix.com', 'github.com', 'stackoverflow.com', 'wikipedia.org',
    'linkedin.com', 'twitter.com', 'instagram.com', 'yahoo.com', 'bing.com',
    'reddit.com', 'medium.com', 'dropbox.com', 'salesforce.com', 'adobe.com'
]

test_urls = [
    'http://example.com',
    'http://example.com',
    'https://www.google.security-update.com',
    'http://faceb00k.com/login',
    'https://google.com',
    'http://microsoft.com',
    'http://bing.com',
    'http://faceb00k.com/login',
    'http://goog1e.com',
    'https://netflix.com'
]


def extract_domain_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix


def is_misspelled_domain(domain, legitimate_domains, threshold=0.9):
    for legit_domain in legitimate_domains:
        legit_domain_name = legit_domain.split('.')[0]
        similarity = lv.ratio(domain, legit_domain_name)
        if similarity >= threshold:
            return False
    return True


def is_phishing_url(url, legitimate_domains, threshold=0.9):
    subdomain, domain, suffix = extract_domain_parts(url)

    if not domain or not suffix:
        print(f"Invalid URL format detected: {url}")
        return True

    full_domain = f"{domain}.{suffix}"

    if full_domain in legitimate_domains:
        print(f"Legitimate URL detected: {url}")
        return False

    if is_misspelled_domain(domain, legitimate_domains, threshold):
        print(f"Potential phishing detected: {url}")
        return True

    print(f"Legitimate URL detected: {url}")
    return False


if __name__ == '__main__':
    # Initial test with predefined URLs
    print("Initial test with predefined URLs:")
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)

    # Interactive loop to scan new URLs
    while True:
        new_url = input("\nEnter a URL to scan (or type 'exit' to quit): ")
        if new_url.lower() == 'exit':
            break
        is_phishing_url(new_url, legitimate_domains)
