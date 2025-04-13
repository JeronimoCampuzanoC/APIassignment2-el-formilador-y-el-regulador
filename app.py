import streamlit as st
import requests

import pandas as pd

API_URL = "http://localhost:8000"  # Change if your FastAPI server is hosted elsewhere

st.title("FastAPI + Streamlit Interface")

# ---- Section 1: Fill (POST) ----
st.header("Fill List (/fill)")
if st.button("Fill my list with strings") :
    response = requests.post(f"{API_URL}/fill")
    if response.status_code == 200 :
        st.success("Strings successfully added!")
    else :
        st.error(f"Failed to add string: {response.text}")

# ---- Section 2: Get Strings ----
st.header("Get All Strings (/get-strings)")
if st.button("Fetch All Strings"):
    response = requests.get(f"{API_URL}/get-strings")
    if response.status_code == 200:
        strings = response.json()
        st.markdown("**Current List of Strings**")
        current_strings = pd.DataFrame(strings)
        st.dataframe (
            current_strings,
            column_config = {
                "Strings: ": st.column_config.TextColumn(width="small")
            },
            hide_index = True,
            use_container_width = False
        )
    else:
        st.error("Failed to fetch strings.")

# ---- Section 3: Filter Strings ----
st.header("Filter Strings (/filter)")
if st.button("Filter"):
    response = requests.get(f"{API_URL}/filter")
    if response.status_code == 200:
        filtered = response.json()
        st.markdown("**Filtered Strings**")
        filtered_data = pd.DataFrame(filtered)
        st.dataframe (
            filtered_data,
            column_config = {
                "Valid Strings: ": st.column_config.TextColumn(width="small")
            },
            hide_index = True,
            use_container_width = False
        )
    else:
        st.error("Failed to filter strings.")

# ---- Section 4: Show Process ----
st.header("Show Process (/show-process)")

if st.button("Show Process"):
    response = requests.get(f"{API_URL}/show-process")
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the response has the expected structure
        if "results" in data:
            for result in data["results"]:
                st.subheader(f"String: '{result['string']}'")
                
                # Sentential Form (Pretty Table)
                st.markdown("**Sentential Derivation**")
                sentential_df = pd.DataFrame(result["sentential"])
                st.dataframe(
                    sentential_df,
                    column_config={
                        "Rule": st.column_config.TextColumn(width="small"),
                        "Sentential": st.column_config.TextColumn(width="large")
                    },
                    hide_index=True,
                    use_container_width=True
                )
                
                # PDA Configuration (Pretty Table)
                st.markdown("**PDA Configuration**")
                config_df = pd.DataFrame(result["configuration"])
                st.dataframe(
                    config_df,
                    column_config={
                        "State": st.column_config.TextColumn(width="small"),
                        "String": st.column_config.TextColumn(width="medium"),
                        "Stack": st.column_config.TextColumn(width="medium")
                    },
                    hide_index=True,
                    use_container_width=True
                )
                
                st.write("---")  # Visual separator
        else:
            st.warning("Unexpected API response format. Showing raw output:")
            st.json(data)
    else:
        st.error(f"Failed to retrieve process output: {response.text}")