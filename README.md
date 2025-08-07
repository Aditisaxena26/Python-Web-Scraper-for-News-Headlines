# 📰 Website News Extractor

This Python-based CLI application allows users to fetch and display news headlines or key titles from **any user-specified website URL**. It leverages the power of `requests` and `BeautifulSoup` for web scraping, providing a simple interface to explore website contents.

## 💡 Features

- Accepts any website URL from the user
- Extracts and displays content from `<title>`, `<h1>`, `<h2>`, and other important tags
- Simple command-line interface
- Supports English and UTF-8 encoded websites

## 🛠️ Tech Stack

- Python
- `requests`
- `beautifulsoup4`

## 🖥️ Sample Output

```bash
Enter the URL of the website to scrape: https://www.TheTimesOfIndia.com
News headlines have been successfully scraped and saved to newsheadlines.txt
Thank you for using the Web Scraper CLI app!
Type OPEN to open the newsheadlines.txt file:- open
                                NEWS HEADLINES
                                ===============
1. India wins historic cricket series against Australia
2. Government announces new education policy
3. Scientists discover Earth-like planet
4. Stock markets rally to new highs
5. Major rainfall expected in North India this week


