import streamlit as st
import plotly.express as px
import pandas as pd

from analysis import label_price, prepare_prices
from llm import get_energy_chain

st.set_page_config(layout="wide")
st.title("Energy Market Insights Assistant")

df = pd.read_csv("data/2025_aer_gas_prices.csv")
df = label_price(df)

# --- Controls ---
unit = st.selectbox("Display units", ["USD/MMBtu", "CAD/GJ"])
df = prepare_prices(df, unit)

# --- Charts ---
st.subheader("Natural Gas Prices")

fig = px.line(df, x="year", y='price', color='hub')
st.plotly_chart(fig, use_container_width=True, theme="streamlit")

# --- Spread ---
st.subheader("Price Spread (Henry Hub – AECO)")

pivot = df.pivot(index="year", columns="hub", values="display_price")
pivot["spread"] = pivot["Henry Hub"] - pivot["AECO-C"]

fig2 = px.line(pivot, y='spread')
st.plotly_chart(fig2, use_container_width=True, theme="streamlit")

# --- LLM ---
st.subheader("Ask the Market Analyst")

chain = get_energy_chain(df)

question = st.text_input(
    "Ask a question about AECO, Henry Hub, or the price spread"
)

if question:
    answer = chain(question)
    st.write(answer)

# --- Footnote ---
st.caption(
    "Source: Alberta Energy Regulator (ST98). Prices are annual averages and include historical and forecast outlook assumptions."
)
st.caption(
    "Daily exchange rate from the Bank of Canada."
)