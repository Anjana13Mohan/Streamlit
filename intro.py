import streamlit as st
st.header("My first app!")
st.write("Learning Streamlit for the first time")
agree= st.checkbox("I agree with Anjana Mohan")
if agree:
    st.write("Great!")
genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")
import random

quotes = [
    "Believe in yourself 💪",
    "Push yourself, no one else is going to do it 🚀",
    "Dream it. Wish it. Do it ✨",
]

st.title("💬 Motivational Quote Generator")

if st.button("Give me a quote!"):
    st.success(random.choice(quotes))
else:
    st.info("Click the button to get a quote!")