import streamlit as st
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

#frontend code
st.title("AI LinkedIn Post Generator")

st.write("Enter a topic and generate a LinkedIn post.")

topic = st.text_input("Enter Topic")

if st.button("Generate LinkedIn Post"):

    prompt_template = f"""
    Write a LinkedIn post about the following topic.

    Topic: {topic}

    Structure the post in the following format:

    1. A catchy intro that grabs attention.
    2. A body consisting of exactly 5 sentences explaining the topic.
    3. A short conclusion that encourages engagement (ask a question or invite opinions).

    Keep the tone professional but engaging.
    Format it nicely for LinkedIn.
    """
    #backend code
    response = chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt_template}
        ]
    )

    st.write(response.choices[0].message.content)
