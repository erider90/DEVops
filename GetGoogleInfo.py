import requests
from bs4 import BeautifulSoup

# Get headline info 

def get_news_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    response = requests.get(
        "https://www.google.com/search?q=us+stock+markets&gl=us&tbm=nws&num=100",
        headers=headers
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    news_articles = []
    for article in soup.find_all('div', class_='SoaBEf'): # Example: Find by div class, may vary
        title_element = article.find('div', class_='MBeuO') # Example: Find title by class
        title = title_element.text.strip() if title_element else "No title"

        source_element = article.find('div', class_='NUnG9d') # Example: Find source by class
        source = source_element.text.strip() if source_element else "No source"

        link_element = article.find('a', href=True) # Example: Find link by anchor tag
        link = link_element['href'] if link_element else "No link"

        news_articles.append({
            "title": title,
            "source": source,
            "link": link,
        })
    return news_articles

news_data = get_news_data()
for article in news_data:
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']}")
    print(f"Link: {article['link']}")
    print("-" * 20)