import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    
    try:
        # Fetch web content
        response = requests.get(url)
        response.check_status() # Check for successful request
        
        # Parseing the html content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find data
        quotes = soup.find_all('div', class_='quote')
        
        scraped_data = []
        
        print(f"--- Scraping: {url} ---\n")
        
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tag = quote.find('div', class_='tags').text.strip()
            
            print(f"Found: {text} - by {author} (Tag: {tag})")
            scraped_data.append([text, author, tag])
            
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()