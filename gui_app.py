# gui_app.py

import tkinter as tk
from tkinter import messagebox

import sys
import os

# Add the src folder to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Now import the fetch_articles function
from article_fetcher import fetch_articles
import json

# Function to fetch and display articles
def fetch_and_display_articles():
    topic = topic_entry.get()
    try:
        page_size = int(articles_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of articles.")
        return
    
    if not topic:
        messagebox.showerror("Invalid Input", "Topic cannot be empty.")
        return
    
    # Fetch articles from NewsAPI
    articles = fetch_articles(topic=topic, page_size=page_size)
    
    if not articles:
        messagebox.showinfo("No Articles", "No articles found for the given topic.")
        return
    
    # Clear the display area
    article_listbox.delete(0, tk.END)
    
    # Display fetched articles in the listbox
    for article in articles:
        article_listbox.insert(tk.END, f"Title: {article['title']}")
        article_listbox.insert(tk.END, f"Description: {article['description']}\n")

    # Optionally, save to a file
    with open("data/articles.json", "w") as f:
        json.dump(articles, f, indent=4)
    
    messagebox.showinfo("Success", "Articles fetched and saved to data/articles.json.")

# Set up the main application window
app = tk.Tk()
app.title("News Aggregator")

# Create input labels and fields
tk.Label(app, text="Enter Topic:").pack(pady=5)
topic_entry = tk.Entry(app, width=50)
topic_entry.pack(pady=5)

tk.Label(app, text="Number of Articles:").pack(pady=5)
articles_entry = tk.Entry(app, width=50)
articles_entry.pack(pady=5)

# Create a button to fetch articles
fetch_button = tk.Button(app, text="Fetch Articles", command=fetch_and_display_articles)
fetch_button.pack(pady=10)

# Create a Listbox to display the articles
article_listbox = tk.Listbox(app, width=70, height=15)
article_listbox.pack(pady=10)

# Run the application
app.mainloop()