# Phishing URL Detector

This Python script helps detect potential phishing URLs by comparing them against a list of legitimate domains. It uses `tldextract` to parse the URL and `Levenshtein` to check for domain name similarities.



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/phishing-url-detector.git
    cd phishing-url-detector
    ```

2. Install the required dependencies:
    ```bash
    pip install tldextract python-Levenshtein
    ```

## Usage

1. **Initial Test**:
    - The script includes an initial test with predefined URLs. Run the script to see the results:
    ```bash
    python phishing_url_detector.py
    ```

2. **Interactive Mode**:
    - After running the initial test, the script enters an interactive mode where you can input URLs to scan. Type `exit` to quit the interactive mode.

## Example

```bash
$ python phishing_url_detector.py
Initial test with predefined URLs:
Legitimate URL detected: http://example.com
Legitimate URL detected: http://example.com
Potential phishing detected: https://www.google.security-update.com
Potential phishing detected: http://faceb00k.com/login
Legitimate URL detected: https://google.com
Legitimate URL detected: http://microsoft.com
Legitimate URL detected: http://bing.com
Potential phishing detected: http://faceb00k.com/login
Potential phishing detected: http://goog1e.com
Legitimate URL detected: https://netflix.com

Enter a URL to scan (or type 'exit' to quit):
