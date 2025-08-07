# web_scraper.py
import requests
from bs4 import BeautifulSoup
# Function to scrape news headlines from a website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code != 200:
            print("Failed to retrieve the page, status code: ",response.status_code)
            return None
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(['h2'])
        # Save the headlines to a text file
        with open("newsheadlines.txt","w",encoding="utf-8") as file:
            file.write("\t\t\t\tNEWS HEADLINES\n")
            file.write("\t\t\t\t"+"="*15+"\n")
            c=1
            for headline in headlines:
                file.write(str(c) + ". " + headline.get_text(strip=True) + "\n")
                c += 1
        print("News headlines have been successfully scraped and saved to newsheadlines.txt")
    except requests.exceptions.RequestException as e:
        print("An error occurred:",e)
        return None
# read_file function to read and print the contents of the newsheadlines.txt file
def read_file():
    with open("newsheadlines.txt", "r",encoding="utf-8") as file:
        headlines = file.read()
        for line in headlines.splitlines():
            print(line)
# main function to handle user input and call the scrape_website and read_file functions
def main():
    url = input("Enter the URL of the website to scrape: ")
    if url:
        scrape_website(url)
    else:
        print("No URL provided. Exiting the scraper.")
    print("Thank you for using the Web Scraper CLI app!")
    user_input = input("Type OPEN to open the newsheadlines.txt file:- ")
    if user_input.upper() == 'OPEN':
        read_file()
    else:
        print("Invalid choice. Exiting the scraper.")
main()