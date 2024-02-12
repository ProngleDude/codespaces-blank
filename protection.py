import re

def filter_content(text_content):
    blacklisted_keywords = ['malware', 'phishing', 'scam', 'virus']  # Define a list of blacklisted keywords

    for keyword in blacklisted_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text_content, re.IGNORECASE):
            return f"Warning: Suspicious keyword '{keyword}' detected in the content. Please proceed with caution."

    return text_content

# Example Usage:
if __name__ == "__main__":
    text_content = "This is a sample text containing malware links. Please be aware of phishing attempts."
    filtered_content = filter_content(text_content)
    print(filtered_content)
