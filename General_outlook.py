import streamlit as st

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
    st.info("This section will display holdings, gains, and analytics.")

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
