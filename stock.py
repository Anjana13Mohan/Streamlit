import streamlit as st
import yfinance as yf
import datetime
import pickle
st.title("Stock price Analyzer")
ticker_data = yf.Ticker("GOOG")
with open('my_streamlit_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Please enter starting date",datetime.date(2023,12,1))
with col2:
    end_date = st.date_input("Please enter ending date",datetime.date(2024,12,1))
ticker_df = ticker_data.history(period='1d',start=start_date,end=end_date)
st.subheader("Here is the raw daywise stock price")
st.dataframe(ticker_df)
st.dataframe(ticker_df.head())
st.subheader("Price movement over time")
st.line_chart(ticker_df['Close'])
st.subheader("Volume movement over time")
st.line_chart(ticker_df['Volume'])

