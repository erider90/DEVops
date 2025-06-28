from gnews import GNews

def get_news_with_gnews(keyword=None, lang='en', country='US', max_results=10):
    """
    Fetches Google News using the GNews library.

    Args:
        keyword (str, optional): The search keyword.
        lang (str): Language code (e.g., 'en', 'es').
        country (str): Country code (e.g., 'US', 'CO').
        max_results (int): Maximum number of results to retrieve.

    Returns:
        list: A list of dictionaries, each representing a news item.
    """
    google_news = GNews(language=lang, country=country, max_results=max_results)

    if keyword:
        news_items = google_news.get_news(keyword)
    else:
        news_items = google_news.get_top_news()

    return news_items

if __name__ == "__main__":
    # Get top news
    print("--- Top Global News Headlines (using GNews) ---")
    top_global_news = get_news_with_gnews(max_results=5)
    for i, news in enumerate(top_global_news):
        print(f"{i+1}. {news['title']}")
        print(f"   Link: {news['url']}")
        print(f"   Published: {news['published date']}")
        print(f"   Description: {news['description']}\n")

