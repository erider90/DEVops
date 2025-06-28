import feedparser

def get_google_news_headlines(query=None, lang='en-US', country='US'):
    """
    Fetches Google News headlines.

    Args:
        query (str, optional): The search query. If None, fetches top headlines.
        lang (str): Language code (e.g., 'en-US', 'es-419').
        country (str): Country code (e.g., 'US', 'CO').

    Returns:
        list: A list of dictionaries, each containing 'title', 'link', 'published', and 'source'.
    """
    if query:
        # For a specific search query
        query_encoded = query.replace(" ", "+")
        url = f"https://news.google.com/rss/search?q={query_encoded}&hl={lang}&gl={country}&ceid={country}:{lang.split('-')[0]}"
    else:
        # For top stories
        url = f"https://news.google.com/rss?hl={lang}&gl={country}&ceid={country}:{lang.split('-')[0]}"

    feed = feedparser.parse(url)

    headlines = []
    for entry in feed.entries:
        headlines.append({
            'title': entry.title,
            # 'link': entry.link,
            'published': entry.published,
            'source': entry.source.title if hasattr(entry, 'source') else 'N/A'
        })
    return headlines

if __name__ == "__main__":
    # Get top headlines for US, English
    print("--- Top US News Headlines ---")
    top_news = get_google_news_headlines(lang='en-US', country='US')
    for i, news in enumerate(top_news[:5]): # Print first 5
        print(f"{i+1}. {news['title']}")
        # print(f"   Link: {news['link']}")
        print(f"   Published: {news['published']}")
        print(f"   Source: {news['source']}\n")

    # Get news headlines for a specific query (e.g., "artificial intelligence") for Colombia, Spanish
    print("\n--- 'Artificial Intelligence' News Headlines (Colombia, Spanish) ---")
    ai_news = get_google_news_headlines(query="inteligencia artificial", lang='es-419', country='CO')
    for i, news in enumerate(ai_news[:5]): # Print first 5
        print(f"{i+1}. {news['title']}")
        # print(f"   Link: {news['link']}")
        print(f"   Published: {news['published']}")
        print(f"   Source: {news['source']}\n")