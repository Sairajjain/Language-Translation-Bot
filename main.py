# Install required libraries
# pip install streamlit googletrans==4.0.0-rc1

import streamlit as st
from googletrans import Translator


# Function to perform translation
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


# Streamlit app
def main():
    st.title("Language Translation Bot")

    # User input
    input_text = st.text_area("Enter text to translate:", "Hello, how are you?")
    target_language = st.selectbox("Select target language:", ["en", "es", "fr", "de", "ja", "ko","te"])

    # Translate button
    if st.button("Translate"):
        if input_text:
            translated_text = translate_text(input_text, target_language)
            st.success(f"Translated text: {translated_text}")
        else:
            st.warning("Please enter text to translate.")


if __name__ == "__main__":
    main()
