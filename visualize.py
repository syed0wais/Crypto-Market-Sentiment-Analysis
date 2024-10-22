# visualize.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment(sentiment_scores):
    sentiment_df = pd.DataFrame(list(sentiment_scores.items()), columns=['Coin', 'Sentiment'])
    
    # Plot a bar chart
    plt.figure(figsize=(8, 4))
    plt.bar(sentiment_df['Coin'], sentiment_df['Sentiment'], color='blue')
    plt.title('Market Sentiment for Cryptocurrencies')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Sentiment Score')
    plt.show()