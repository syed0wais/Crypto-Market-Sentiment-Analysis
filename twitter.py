pip install tweepy textblob


import tweepy
from textblob import TextBlob

# Twitter API credentials
api_key = "YOUR_API_KEY"
api_key_secret = "YOUR_API_KEY_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to fetch tweets and analyze sentiment
def fetch_crypto_sentiment(crypto_keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=crypto_keyword, lang="en", tweet_mode="extended").items(count)
    
    positive, neutral, negative = 0, 0, 0
    for tweet in tweets:
        # Use TextBlob for sentiment analysis
        analysis = TextBlob(tweet.full_text)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity == 0:
            neutral += 1
        else:
            negative += 1

    total = positive + neutral + negative
    print(f"Sentiment analysis for '{crypto_keyword}' in {total} tweets:")
    print(f"Positive: {positive/total:.2%}")
    print(f"Neutral: {neutral/total:.2%}")
    print(f"Negative: {negative/total:.2%}")

# Example usage for Bitcoin sentiment analysis
fetch_crypto_sentiment("Bitcoin", count=100)
