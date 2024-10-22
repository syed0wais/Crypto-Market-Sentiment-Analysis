# main.py

from fetch_data import fetch_crypto_data
from sentiment_analysis import get_sentiment, simulate_market_sentiments
from visualize import plot_sentiment

def crypto_sentiment_analysis():
    # Fetch data
    crypto_data = fetch_crypto_data()
    
    # Simulate market sentiments
    market_sentiments = simulate_market_sentiments()
    
    # Analyze sentiments
    sentiment_scores = {}
    for coin in crypto_data:
        name = coin['name']
        if name in market_sentiments:
            sentiment_scores[name] = get_sentiment(market_sentiments[name])

    # Visualize the results
    plot_sentiment(sentiment_scores)

# Main execution
if __name__ == '__main__':
    crypto_sentiment_analysis()
