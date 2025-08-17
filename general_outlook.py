# general_outlook.py

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AlfaQ-X Portfolio Dashboard", layout="wide")

st.title("📊 AlfaQ-X Portfolio Dashboard")
st.markdown("An interactive dashboard for monitoring your stock portfolio.")

# --- Portfolio Stocks (Dummy / Replace with live list) ---
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# --- Fetch Latest Data ---
try:
    data = yf.download(stocks, period="3mo")["Adj Close"]
    
    # Handle multi-index from yfinance
    if isinstance(data, pd.DataFrame) and isinstance(data.columns, pd.MultiIndex):
        data = data.droplevel(0, axis=1)

    latest_prices = data.iloc[-1].to_dict()
except Exception as e:
    st.error(f"⚠️ Error fetching prices: {e}")
    data = pd.DataFrame()
    latest_prices = {s: None for s in stocks}

# --- Layout ---
col1, col2 = st.columns([1, 2])

# Portfolio Summary
with col1:
    st.subheader("📌 Portfolio Summary")
    portfolio_value = 0
    for s in stocks:
        price = latest_prices.get(s, None)
        if price:
            portfolio_value += price
        st.write(f"**{s}**: {price:.2f}" if price else f"**{s}**: N/A")
    st.markdown(f"### 💰 Total Portfolio Value: ${portfolio_value:,.2f}")

# Performance Chart
with col2:
    st.subheader("📈 Performance (Last 3 Months)")
    if not data.empty:
        fig, ax = plt.subplots(figsize=(10, 5))
        data.plot(ax=ax)
        plt.title("Stock Prices (Adj Close)")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        st.pyplot(fig)
    else:
        st.warning("No data available to display chart.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Powered by **AlfaQ-X**")


