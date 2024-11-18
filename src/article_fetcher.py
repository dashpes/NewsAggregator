import requests
from collections import defaultdict
from datetime import datetime, timedelta
from config import API_KEY, BASE_URL

def fetch_articles(topic='world', page_size=30, last_week_only=False, max_articles_per_source=2): 
    """
    Fetch articles from NewsAPI based on a topic and optional date range.
    
    Parameters:
    - topic (str): Topic to search for articles.
    - page_size (int): Number of articles to fetch.
    - last_week_only (bool): If True, limit results to the past week.
    - max_articles_per_source (int): Maximum number of articles to include per source.

    Returns:
    - List of cleaned articles.
    """
    url = f"{BASE_URL}everything"
    
    # Set date range if last_week_only is True
    if last_week_only:
        today = datetime.now()
        last_week = today - timedelta(days=7)
        from_date = last_week.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')
    else:
        from_date = None
        to_date = None

    params = {
        'q': topic,
        'apiKey': API_KEY,
        'pageSize': page_size,
        'from': from_date,
        'to': to_date
    }
    
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching data:", response.json().get("message"))
        return []

    # Parse articles
    articles = response.json().get('articles', [])
    
    # Group and filter articles by source
    grouped_articles = defaultdict(list)
    for article in articles:
        source_name = article['source']['name']
        grouped_articles[source_name].append(article)
    
    # Limit articles per source
    cleaned_articles = []
    for source, articles_list in grouped_articles.items():
        cleaned_articles.extend(articles_list[:max_articles_per_source])
    
    return cleaned_articles