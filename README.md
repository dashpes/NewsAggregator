# **News Aggregator**

A Python-based News Aggregator application that fetches the latest news articles on a given topic from the NewsAPI and stores the results in a JSON file. It includes functionality to filter articles by topic, limit articles from specific sources, and specify date ranges (e.g., only from the past week). 

---

## **Features**
- Fetch articles from NewsAPI based on a specified topic.
- Filter articles by date range (e.g., last week).
- Limit the number of articles fetched per source.
- Save the fetched articles to a JSON file for offline use.
- Display fetched articles with their titles, descriptions, and source.

---

## **Requirements**
- Python 3.8+
- NewsAPI account and API key (to fetch news articles). See more here: [NewsAPILink](https://newsapi.org/)
- Installed Python packages (see the **Setup** section below).

---

## **Setup**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/news-aggregator.git
   cd news-aggregator
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Add Your API Key**
   Create a file named config.py in the src folder if not pulled from the repo
   ```bash
   API_KEY = "your_newsapi_key_here"
   BASE_URL = "https://newsapi.org/v2/"

---

## **Usage**
1.	Run the program to fetch news articles on a specific topic.
2.	Articles will be saved to data/articles.json.
3.	Customize the topic, page size, or other parameters in the main.py file:
```bash
  topic = 'Technology'       # Replace with your topic of interest
  page_size = 20             # Number of articles to fetch
  last_week_only = True      # Fetch articles from the last week only
  max_articles_per_source = 3  # Limit articles per source
```
---

## **Acknowledgements**
NewsAPI for providing the news data.
The Python community for creating incredible libraries and tools.

---
