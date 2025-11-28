import requests
from bs4 import BeautifulSoup

def get_sl_news():
    # URL 1: Daily Mirror (Primary)
    url = "https://www.dailymirror.lk/latest-news/108"
    # URL 2: Adaderana (Backup - if URL 1 fails)
    backup_url = "http://www.adaderana.lk/hot-news/"
    
    headlines = []
    
    try:
        # Try Primary Source
        response = requests.get(url, timeout=5) # 5 second timeout
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all('h3', limit=8):
            text = item.get_text(strip=True)
            if len(text) > 15: headlines.append(text)
            
    except Exception as e:
        print(f"Primary source failed: {e}")
        # If primary fails, return a dummy list so the app doesn't look empty
        headlines = [
            "⚠️ Connection Error: Could not fetch live news.",
            "Ensure you have an active internet connection."
        ]
        
    return headlines