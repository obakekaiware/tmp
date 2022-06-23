import os
import json
import streamlit as st


if __name__ == "__main__":
    path = os.path.join("data", "text.json")
    if os.path.exists(path):
        with open(path) as file:
            texts = json.load(file)
    else:
        texts = []

    text = st.text_input("text")
    texts.append(text)

    if st.button("Save"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as file:
            json.dump(texts, file, indent=4)
