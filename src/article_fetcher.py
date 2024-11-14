import requests
from datetime import datetime, timedelta
from config import API_KEY, BASE_URL

def fetch_articles(topic='world', page_size=10, last_two_weeks=False): 
    """
    Fetch articles from NewsAPI based on a topic and optional date range.
    
    Default topic is 'world' and page_size is '10'. Optionally limits to articles from the past week.
    """
    url = f"{BASE_URL}everything"
    
    # Set date range if last_two_weeks is True
    if last_two_weeks:
        today = datetime.now()
        last_week = today - timedelta(days=14)
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
    
    data = response.json()
    return data.get('articles', [])