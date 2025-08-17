import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="AlfaIQ-X",
    page_icon="📈",
    layout="wide"
)

# --- Sidebar Navigation ---
st.sidebar.title("AlfaIQ-X Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Portfolio Dashboard", "🔮 Stock Predictor", "📈 Live Markets", "⚙️ Settings"])

# --- Home Page ---
if page == "🏠 Home":
    st.title("Welcome to AlfaIQ-X 🚀")
    st.subheader("Smart Investing. Seamless Insights.")
    st.write("""
        AlfaIQ-X is your intelligent companion for trading and asset valuation.  
        Navigate through the menu to explore:
        - **Portfolio Dashboard**: Track performance of your assets  
        - **Stock Predictor**: AI-driven stock forecasting  
        - **Live Markets**: Real-time NYSE & NGX market data  
    """)

# --- Portfolio Dashboard ---
elif page == "📊 Portfolio Dashboard":
    st.title("📊 Portfolio Dashboard")
    st.write("Track your portfolio performance in real-time with live market data.")

    # --- Define Portfolio ---
    portfolio = {
        "AAPL": 50,
        "MSFT": 30,
        "GOOGL": 20,
        "TSLA": 10,
        "AMZN": 15
    }

    # --- Fetch Live Prices ---
    stocks = list(portfolio.keys())
    data = yf.download(stocks, period="1d")["Adj Close"].iloc[-1]

    # --- Build DataFrame ---
    df = pd.DataFrame({
        "Stock": stocks,
        "Quantity": [portfolio[s] for s in stocks],
        "Current Price": [data[s] for s in stocks]
    })
    df["Buy Price"] = [150, 280, 2500, 700, 3300]  # example fixed buy prices
    df["Value"] = df["Quantity"] * df["Current Price"]
    df["Gain/Loss %"] = ((df["Current Price"] - df["Buy Price"]) / df["Buy Price"]) * 100

    # --- Display Table ---
    st.subheader("Portfolio Holdings (Live)")
    st.dataframe(df.style.format({
        "Buy Price": "${:,.2f}",
        "Current Price": "${:,.2f}",
        "Value": "${:,.2f}",
        "Gain/Loss %": "{:.2f}%"
    }))

    # --- Portfolio Value Over Time ---
    st.subheader("Portfolio Performance (Last 3 Months)")
    hist = yf.download(stocks, period="3mo")["Adj Close"]
    portfolio_value = (hist * pd.Series(portfolio)).sum(axis=1).reset_index()
    portfolio_value.columns = ["Date", "Portfolio Value"]

    line_chart = px.line(portfolio_value, x="Date", y="Portfolio Value", title="Portfolio Growth Over Time")
    st.plotly_chart(line_chart, use_container_width=True)

    # --- Asset Allocation Pie Chart ---
    st.subheader("Asset Allocation")
    pie_chart = px.pie(df, values="Value", names="Stock", title="Portfolio Distribution")
    st.plotly_chart(pie_chart, use_container_width=True)

# --- Stock Predictor ---
elif page == "🔮 Stock Predictor":
    st.title("🔮 Stock Predictor")
    st.write("AI-driven forecasts for short and medium-term stock performance.")
    st.warning("Prediction model integration coming soon.")

# --- Live Markets ---
elif page == "📈 Live Markets":
    st.title("📈 Live Markets")
    st.write("Streaming data from global exchanges (NYSE, NGX).")
    st.success("Live data integration will appear here.")

# --- Settings ---
elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.write("Customize AlfaIQ-X experience: themes, alerts, API keys, etc.")

