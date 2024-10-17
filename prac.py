import streamlit as st

st.title("Currency Converter")

# Static exchange rates
exchange_rates = {
    "USD": 1.0,  # Base currency
    "EUR": 0.9,
    "GBP": 0.8,
    "JPY": 140.0,
    "BTC": 30000.0,  
    "PKR": 278.48  # Example Bitcoin rate
}

# Get user input
from_currency = st.selectbox("From Currency", list(exchange_rates.keys()), index=0)
to_currency = st.selectbox("To Currency", list(exchange_rates.keys()), index=0)
amount = st.number_input("Amount", min_value=0.01, step=0.01)

# Centered convert button
if st.button("Convert", key="convert_btn"):
    try:
        converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
        st.success(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
