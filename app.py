import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Stock Market Data Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Market Data Analyzer")

uploaded_file = st.file_uploader(
    "Upload Stock CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df["Date"] = pd.to_datetime(df["Date"])

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    # Metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Closing Price",
            f"{df['Close'].max():.2f}"
        )

    with col2:
        st.metric(
            "Lowest Closing Price",
            f"{df['Close'].min():.2f}"
        )

    # Moving Average
    df["MA20"] = df["Close"].rolling(20).mean()

    # Closing Price Chart
    st.subheader("Closing Price Trend")

    fig1, ax1 = plt.subplots()
    ax1.plot(df["Date"], df["Close"])
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close Price")
    st.pyplot(fig1)

    # Moving Average Chart
    st.subheader("Moving Average (20 Days)")

    fig2, ax2 = plt.subplots()
    ax2.plot(df["Date"], df["Close"], label="Close")
    ax2.plot(df["Date"], df["MA20"], label="MA20")
    ax2.legend()
    st.pyplot(fig2)

    # Volume Chart
    st.subheader("Trading Volume")

    fig3, ax3 = plt.subplots()
    ax3.bar(df["Date"], df["Volume"])
    ax3.set_ylabel("Volume")
    st.pyplot(fig3)