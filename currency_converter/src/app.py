from src.main import get_exchange_rate, calculate_conversion, get_relative_time, get_all_supported_currencies
import streamlit as st
st.title("Currency Converter")
currencies = get_all_supported_currencies()
currency_dict = {code: name for code, name in currencies}
columns = st.columns(2)
base_currency = columns[0].selectbox("Select base currency", options=currency_dict.keys(), format_func=lambda x: f"{x} - {currency_dict[x]}")
target_currency = columns[1].selectbox("Select target currency", options=currency_dict.keys(), format_func=lambda x: f"{x} - {currency_dict[x]}")
amount = st.number_input("Enter amount to convert", min_value=0.0, format="%.2f")

if amount > 0: 
    rate, last_updated, last_updated_unix = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = calculate_conversion(amount, rate)
        st.success(f"{amount} {base_currency} is equal to {converted_amount} {target_currency} at an exchange rate of {rate}.")
        relative_time = get_relative_time(last_updated_unix)
        st.info(f'Last updated exchange rate from {base_currency} to {target_currency} is {relative_time}')
    else:
        st.error(f"Exchange rate for {target_currency} not found.")