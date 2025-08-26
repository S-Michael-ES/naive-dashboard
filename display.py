import streamlit as st
import requests
import pandas as pd

BASE_API_URL = "https://naive-api.herokuapp.com"

st.set_page_config(page_title="Naive Streaming", layout="wide")
st.title("Naive Streaming")

st.subheader("About")
st.markdown("""
Howdy!
I created this project to implement skills and technologies I have learned in university into a personal project.
            
Music is a huge passion of mine, so I wanted to create a custom space where my friends and I could upload and listen to our music.
""")

st.subheader("Updates")
st.markdown("""
Ver 0.2:
- Hosted backend with Heroku
- Published frontend with Streamlit

""")
st.markdown("""
Ver 0.1:
- PostGreSQL database
- Flask backend
- Streamlit frontend

""")

st.header("All Tracks")

try:
    TRACKS_API_URL = f"{BASE_API_URL}/api/tracks"
    
    response = requests.get(TRACKS_API_URL)
    response.raise_for_status()
    
    tracks_data = response.json()

    if tracks_data:
        for track in tracks_data:
            st.markdown(f"**{track['artist']}** - {track['title']}")
            
            st.audio(track['audio_url'])
            
            st.divider() 
    else:
        st.write("No tracks found.")

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the API. Error: {e}")