import requests
from bs4 import BeautifulSoup

def make_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])  # Extract text from <p> tags
    return text

def scrape_website(url):
    html_content = make_request(url)
    if html_content:
        text_content = extract_text(html_content)
        return text_content
    else:
        return None

# Example Usage:
if __name__ == "__main__":
    url = "https://example.com"
    scraped_text = scrape_website(url)
    if scraped_text:
        print(f"Text content from {url}:\n{scraped_text}")
