import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Change if your FastAPI server is hosted elsewhere

st.title("FastAPI + Streamlit Interface")

# ---- Section 1: Fill (POST) ----
st.header("Add a String (/fill)")
with st.form(key='fill_form'):
    input_text = st.text_input("Enter a string to fill:")
    submit_fill = st.form_submit_button("Send to /fill")
    if submit_fill:
        response = requests.post(f"{API_URL}/fill", json={"text": input_text})
        if response.status_code == 200:
            st.success("String successfully added!")
        else:
            st.error(f"Failed to add string: {response.text}")

# ---- Section 2: Get Strings ----
st.header("Get All Strings (/get-strings)")
if st.button("Fetch All Strings"):
    response = requests.get(f"{API_URL}/get-strings")
    if response.status_code == 200:
        strings = response.json()
        st.write(strings)
    else:
        st.error("Failed to fetch strings.")

# ---- Section 3: Filter Strings ----
st.header("Filter Strings (/filter)")
query = st.text_input("Filter query:")
if st.button("Filter"):
    response = requests.get(f"{API_URL}/filter", params={"query": query})
    if response.status_code == 200:
        filtered = response.json()
        st.write(filtered)
    else:
        st.error("Failed to filter strings.")
