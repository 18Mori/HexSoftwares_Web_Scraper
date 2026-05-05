import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    
    try:
        # Fetch web content
        response = requests.get(url)
        response.raise_for_status() # Check for successful request
        
        # Parseing the html content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find data
        quotes = soup.find_all('div', class_='quote')
        
        scraped_data = []
        
        print(f"--- Scraping: {url} ---\n")
        
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            
            print(f"Found: {text} \n- by {author} \n")
            print("-" * 100 + "\n")
            scraped_data.append([text, author])
            
        # Save data to CSV file
        save_to_csv(scraped_data)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def save_to_csv(data):
    filename = "scraped_quotes.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"]) # Header
        writer.writerows(data)
    print(f"\nSuccess! Data saved to {filename}")

if __name__ == "__main__":
    scrape_quotes()