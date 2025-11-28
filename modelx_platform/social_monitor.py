import feedparser
import sys
def get_reddit_trends():
    # URL for r/srilanka top posts of the week (RSS Feed)
    rss_url = "https://www.reddit.com/r/srilanka/top/.rss?t=week"
    
    posts_data = []
    try:
        feed = feedparser.parse(rss_url)
        
        # Loop through the first 10 entries
        for entry in feed.entries[:10]:
            posts_data.append({
                "title": entry.title,
                # RSS doesn't give exact score, but order implies popularity
                "link": entry.link
            })
            
    except Exception as e:
        print(f"Error reading RSS feed: {e}")
        
    return posts_data

# Test it immediately
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8') 
    print(get_reddit_trends())