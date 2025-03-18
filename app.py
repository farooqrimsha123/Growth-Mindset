#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("♛ Welcome to Your Growth Journey!")
st.write("Growth mindset challenge: Embrace setbacks as opportunities to learn and improve!")

#quote section
st.header("🌞 Today's Growth Mindset Quote")
st.write("""Challenges are growth in disguise—embrace them!""")

st.header("🗝️ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f"💪You're facing: {user_input}. Keep pushing forward towards your goal!✌" )
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨Great Insight!Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


#achievements
st.header("🏆Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"💫Amazing!You achieved: {achievement}")
else:
    st.info("Big or small , every achievement counts! Share one now🤩")

#footer        
st.write("- - -")
st.write("""🥇Push beyond limits—every challenge is a step toward growth!🌠""")
st.write("©Created by Rimsha Farooq")
