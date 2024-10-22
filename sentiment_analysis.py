# sentiment_analysis.py

from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def simulate_market_sentiments():
    return {
        "Bitcoin": "Bitcoin reaches a new all-time high, exciting investors.",
        "Ethereum": "Ethereum developers are concerned about delays in the 2.0 upgrade.",
        "Dogecoin": "Dogecoin price falls after social media hype dies down."
    }
