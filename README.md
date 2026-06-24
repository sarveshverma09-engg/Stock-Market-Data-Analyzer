# 📈 Stock Market Data Analyzer

A Streamlit-based web application that allows users to upload stock market CSV data and perform basic analysis with interactive visualizations.

## Features

* Upload stock market CSV files
* Preview dataset
* View summary statistics
* Display highest and lowest closing prices
* Calculate 20-day Moving Average (MA20)
* Visualize:

  * Closing Price Trend
  * 20-Day Moving Average
  * Trading Volume

## Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/stock-market-data-analyzer.git
cd stock-market-data-analyzer
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

## CSV Format

The uploaded CSV file should contain the following columns:

| Date       | Close  | Volume  |
| ---------- | ------ | ------- |
| 2024-01-01 | 150.25 | 1200000 |
| 2024-01-02 | 152.80 | 1350000 |

## Analysis Provided

### Summary Statistics

Displays statistical information such as:

* Mean
* Standard Deviation
* Minimum Value
* Maximum Value

### Closing Price Trend

Visualizes stock closing prices over time.

### 20-Day Moving Average

Calculates and plots the 20-day moving average alongside closing prices.

### Trading Volume Analysis

Displays daily trading volume using a bar chart.

## Future Improvements

* Multiple stock comparison
* Candlestick charts
* Technical indicators (RSI, MACD)
* Downloadable analysis reports
* Interactive Plotly visualizations

## Author

Sarvesh Verma
