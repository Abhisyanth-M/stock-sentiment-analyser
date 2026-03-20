import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer= SentimentIntensityAnalyzer()
st.set_page_config(page_title="Stock Sentiment Analyzer", page_icon="📈")
st.title("📈 Stock News Sentiment Analyser")
st.markdown("Enter any stock name to analyse latest news sentiment!")
stock = st.text_input("Enter Stock Name", placeholder="e.g. Infosys, TCS, Reliance")

def get_news(stock_name):
    url = f"https://news.google.com/search?q={stock_name}+stock&hl=en-IN&gl=IN"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all("a", class_="JtKRv")
    return [h.text for h in headlines[:10]]

def analyse_sentiment(headlines):
    results = []
    for headline in headlines:
        score = analyzer.polarity_scores(headline)
        compound = score["compound"]
        if compound >= 0.05:
            sentiment = "🟢 Positive"
        elif compound <= -0.05:
            sentiment = "🔴 Negative"
        else:
            sentiment = "🟡 Neutral"
        results.append({"Headline": headline, "Sentiment": sentiment, "Score": compound})
    return pd.DataFrame(results)

# Main app logic
if stock:
    with st.spinner(f"Fetching latest news for {stock}..."):
        headlines = get_news(stock)
    
    if not headlines:
        st.error("No news found! Try a different stock name.")
    else:
        df = analyse_sentiment(headlines)
        
        # Overall sentiment
        avg_score = df["Score"].mean()
        if avg_score >= 0.05:
            overall = "🟢 Bullish — Consider Buying!"
        elif avg_score <= -0.05:
            overall = "🔴 Bearish — Consider Selling!"
        else:
            overall = "🟡 Neutral — Hold!"
        
        st.subheader("Overall Sentiment")
        st.metric("Signal", overall)
        st.metric("Average Score", f"{avg_score:.2f}")
        
        st.subheader("Latest News Headlines")
        st.dataframe(df, use_container_width=True)