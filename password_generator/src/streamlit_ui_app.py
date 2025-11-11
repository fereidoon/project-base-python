import streamlit as st
from src.PassGeneratorClass import PinGenerator ,RandomPasswordGenerator,MemorablePasswordGenetator
st.title("Password and PIN Generator")
st.image("./src/image/banner.jpeg")
st.write("Welcome to the Password and PIN Generator App! Choose your preferred method below to generate secure credentials.")
user_chosen_metod = st.selectbox("Select Generation Method", 
                                 ("PIN Generator", "Random Password Generator", "Memorable Password Generator"))    
if user_chosen_metod == "PIN Generator":
    st.header("PIN Generator")
    pin_length = st.slider("Select PIN Length", min_value=4, max_value=12, value=4)
    generator = PinGenerator(length=pin_length)
elif user_chosen_metod == "Random Password Generator":
    st.header("Random Password Generator")
    password_length = st.slider("Select Password Length", min_value=8, max_value=32, value=12)
    include_punctuation = st.toggle("Include Punctuation", value=False)
    include_numbers = st.toggle("Include Numbers", value=False)
    generator = RandomPasswordGenerator(length=password_length,
                                        include_punctuation=include_punctuation,
                                        include_numbers=include_numbers)
elif user_chosen_metod == "Memorable Password Generator":
    st.header("Memorable Password Generator")
    number_of_words = st.slider("Select Number of Words", min_value=2, max_value=6, value=4)
    seperator = st.text_input("Word Separator", value="_")
    capitilaze = st.toggle("Randomly Capitilize Words", value=False)
    generator = MemorablePasswordGenetator(number_of_words=number_of_words,
                                           seperator=seperator,
                                           capitilaze=capitilaze)
password = generator.generate()
st.subheader("Generated Credential:")
st.header(fr"``` {password} ```")
st.success("Your credential has been generated successfully!")









