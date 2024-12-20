import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.models import load_model # type: ignore
import matplotlib.pyplot as plt
import yfinance as yf

st.title("StockVision App(Stock Predictor)")

stock = st.selectbox('Enter the Stock ID',('GOOG', 'RGTI', 'NVDA','TSLA','PLTR','SMCI','LCID','SOUN','INTC','UBER','BBD','WBA','GSAT','Other'))
if stock=="Other":
    otherOption =st.text_input("Enter the Stock ID:")
    if not otherOption:  # Check if the input is empty
        st.warning("Please enter a valid Stock ID.")
    else:
        stock = otherOption 

from datetime import datetime
end = datetime.now()
start = datetime(end.year-20,end.month,end.day)

google_data = yf.download(stock, start, end)
google_data.columns = google_data.columns.to_flat_index()
google_data.columns = [col[0] for col in google_data.columns]
model = load_model("Latest_stock_price_model.keras")
st.subheader(f"{stock} Stock Dataset")
st.write(google_data)

splitting_len = int(len(google_data)*0.7)
x_test = pd.DataFrame(google_data.Close[splitting_len:])

def plot_graph(figsize, values, full_data, extra_data = 0, extra_dataset = None):
    fig = plt.figure(figsize=figsize)
    plt.plot(values,'Orange')
    plt.plot(full_data.Close, 'b')
    if extra_data:
        plt.plot(extra_dataset)
    return fig

st.subheader(f"{stock}'s Original Close Price and MA for 250 days")
google_data['MA_for_250_days'] = google_data.Close.rolling(250).mean()
st.pyplot(plot_graph((15,6), google_data['MA_for_250_days'],google_data,0))

st.subheader(f"{stock}'s Original Close Price and MA for 200 days")
google_data['MA_for_200_days'] = google_data.Close.rolling(200).mean()
st.pyplot(plot_graph((15,6), google_data['MA_for_200_days'],google_data,0))

st.subheader(f"{stock}'s Original Close Price and MA for 100 days")
google_data['MA_for_100_days'] = google_data.Close.rolling(100).mean()
st.pyplot(plot_graph((15,6), google_data['MA_for_100_days'],google_data,0))

st.subheader('Original Close Price and MA for 100 days and MA for 250 days')
st.pyplot(plot_graph((15,6), google_data['MA_for_100_days'],google_data,1,google_data['MA_for_250_days']))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(x_test[['Close']])

x_data = []
y_data = []

for i in range(100,len(scaled_data)):
    x_data.append(scaled_data[i-100:i])
    y_data.append(scaled_data[i])

x_data, y_data = np.array(x_data), np.array(y_data)

predictions = model.predict(x_data)

inv_pre = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_data)

ploting_data = pd.DataFrame(
 {
  'original_test_data': inv_y_test.reshape(-1),
    'predictions': inv_pre.reshape(-1)
 } ,
    index = google_data.index[splitting_len+100:]
)
st.subheader("Original values vs Predicted values")
st.write(ploting_data)

st.subheader('Original Close Price vs Predicted Close price')
fig = plt.figure(figsize=(15,6))
plt.plot(pd.concat([google_data.Close[:splitting_len+100],ploting_data], axis=0))
plt.legend(["Data- not used", "Original Test data", "Predicted Test data"])
st.pyplot(fig)


st.write("Developed By KishorForgge")