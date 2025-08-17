import streamlit as st
import pandas as pd
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
    st.write("Track your portfolio performance in real-time.")

    # --- Dummy Portfolio Data ---
    data = {
        "Stock": ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"],
        "Quantity": [50, 30, 20, 10, 15],
        "Buy Price": [150, 280, 2500, 700, 3300],
        "Current Price": [170, 300, 2700, 750, 3500]
    }
    df = pd.DataFrame(data)
    df["Value"] = df["Quantity"] * df["Current Price"]
    df["Gain/Loss %"] = ((df["Current Price"] - df["Buy Price"]) / df["Buy Price"]) * 100

    # --- Display Table ---
    st.subheader("Portfolio Holdings")
    st.dataframe(df.style.format({"Buy Price": "${:,.2f}", "Current Price": "${:,.2f}", "Value": "${:,.2f}", "Gain/Loss %": "{:.2f}%"}))

    # --- Portfolio Performance Chart ---
    st.subheader("Portfolio Performance (Dummy Trend)")
    perf_data = pd.DataFrame({
        "Date": pd.date_range(start="2024-05-01", periods=6, freq="M"),
        "Portfolio Value": [25000, 26500, 27000, 29000, 31000, 33000]
    })
    line_chart = px.line(perf_data, x="Date", y="Portfolio Value", title="Portfolio Growth Over Time")
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

