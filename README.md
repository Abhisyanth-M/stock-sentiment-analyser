# Stock News Sentiment Analyser

A real-time NLP web app that scrapes latest stock news headlines and analyses sentiment to generate Buy, Sell or Hold signals for retail investors.

## Live Demo
https://huggingface.co/spaces/Abhisyanth-M/stock-sentiment-analyser

## Problem Statement
Over 5 crore retail investors in India make stock buying and selling decisions based on emotion, tips from friends, or random forwards — not data. When news breaks about a company, most investors do not know how to interpret it quickly and either panic sell or FOMO buy at the wrong time.

## Solution
A real-time sentiment analysis app that scrapes the latest news headlines for any stock, analyses each headline using NLP, and gives an overall Buy, Sell or Hold signal in seconds.

## Features
- Real-time news scraping for any stock
- NLP sentiment analysis on each headline
- Overall Buy, Sell or Hold signal with average score
- Sentiment breakdown table for each headline
- Positive, Negative and Neutral classification

## Tech Stack
- Python
- VADER Sentiment Analysis
- BeautifulSoup
- Requests
- Streamlit
- Pandas

## How it Works
- User enters any stock name
- App scrapes latest news headlines from Google News
- VADER NLP model analyses each headline
- Compound score calculated for each headline
- Overall average score determines Buy, Sell or Hold signal

## Sentiment Score Logic
- Score above 0.05 — Positive
- Score below -0.05 — Negative
- Score between -0.05 and 0.05 — Neutral

## How to Run Locally
```bash
git clone https://github.com/Abhisyanth-M/stock-sentiment-analyser
cd stock-sentiment-analyser
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Limitations
- Sentiment analysis is based on headline text only — not full article content
- Google News scraping may break if website structure changes
- VADER is a general purpose sentiment model — not finance specific
- Should not be used as the sole basis for investment decisions

## Disclaimer
This app is for educational purposes only. Always do your own research before making investment decisions.

## GitHub
https://github.com/Abhisyanth-M/stock-sentiment-analyser
