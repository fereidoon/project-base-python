import streamlit as st

from src.password_generator import pin_generator, password_generator, memorable_password_genetator

st.title("password generator")
st.image("./src/image/banner.jpeg")
user_choise = st.radio("Select Password Type",("PIN Generator","Random Password Generator","Memorable Password Generator"))
if user_choise == "PIN Generator":
    length = st.slider("Select PIN Length",4,12,4)
    if st.button("Generate PIN"):
        pin = pin_generator(length)
        st.success(f"Generated PIN: {pin}")
if user_choise == "Random Password Generator":
    length = st.slider("Select Password Length",8,24,12)
    punctuation = st.checkbox("Include Punctuation",False)
    numbers = st.checkbox("Include Numbers",False)
    if st.button("Generate Password"):
        password = password_generator(length,punctuation,numbers)
        st.success(f"Generated Password: {password}")
if user_choise == "Memorable Password Generator":
    number_of_words = st.slider("Select Number of Words",2,6,4)
    seperator = st.text_input("Enter Separator","_")
    capitilaze = st.checkbox("Randomly Capitalize Words",False)
    if st.button("Generate Memorable Password"):
        memorable_password = memorable_password_genetator(number_of_words,seperator,capitilaze)
        st.success(f"Generated Memorable Password: ``` {memorable_password} ```")
