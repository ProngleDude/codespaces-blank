from scraper import scrape_website
from protection import filter_content

def main():
    print("Prongle Scraper!\n")
    target_url = input("Where shall I prongle: ")

    scraped_text = scrape_website(target_url)
    if scraped_text:
        filtered_content = filter_content(scraped_text)
        print("\nFiltered Content:")
        print(filtered_content)
    else:
        print("Failed to scrape content from the specified website. Please check the URL and try again.")

if __name__ == "__main__":
    main()
