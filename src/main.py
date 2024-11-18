from article_fetcher import fetch_articles
import json

def main():
    # Fetch articles on a specific topic
    topic = 'Trump'
    articles = fetch_articles(topic=topic, page_size=30, last_week_only=True, max_articles_per_source=2)

    # Display the fetched articles
    if articles:
        print(f"Fetched {len(articles)} articles about {topic}.\n")
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}\n")
    else:
        print("No articles found.")

    # Optionally, save to a file
    with open("data/articles.json", "w") as f:
        json.dump(articles, f, indent=4)
        print("\nArticles saved to data/articles.json.")

if __name__ == "__main__":
    main()