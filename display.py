import streamlit as st
import requests
import pandas as pd

# Define the URL of your Flask API
FLASK_API_URL = "https://naive-api-314809ea71f0.herokuapp.com/api/artists"

st.set_page_config(page_title="Naive Streaming", layout="wide")
st.title("Naive Streaming")

st.subheader("About")
st.markdown("""
Howdy!
I created this project to implement skills and technologies I have learned in university into a personal project.
            
Music is a huge passion of mine, and I found inspiration in the shortcomings and backlash facing streaming platforms today.
""")

st.subheader("Updates")
st.markdown("""
Ver 0.1:
This version implements:
- PostGreSQL database
- Flask backend
- Streamlit frontend

""")

# --- Fetch and Display Data ---
try:
    # Make a request to the API
    response = requests.get(FLASK_API_URL)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    
    artists_data = response.json()

    if artists_data:
        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(artists_data)
        
        # Display the data in a table
        st.dataframe(df, use_container_width=True)
    else:
        st.write("No artists found.")

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the API. Make sure the Flask server is running. Error: {e}")