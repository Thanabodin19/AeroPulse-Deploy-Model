import streamlit as st
import pandas as pd
import requests

def getRawData():
    url = "http://localhost:8000/rawdata"  # FastAPI runs on port 8000
    response = requests.get(url)
    return response

if __name__ == "__main__":
    st.set_page_config(layout='wide', page_title="AeroPulse Visualization", page_icon="✈️")
    
    # Create a container
    with st.container():
        # Create two columns
        col1, col2 = st.columns([6, 0.7])
        with col1:
            st.title("AeroPulse ✈️")
            st.markdown("**- Classify Satisfaction, Neutral or Dissatisfaction of passenger based on history data -**")
        with col2:
            st.write("")
            if st.button("Summarize The Flight 🧑🏻‍✈️", type="primary"):
                res = getRawData()
            else:
                res = None

        st.markdown(
            """
            <style>
            .stTabs [role="tablist"] {
                margin-top: 30px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        tab1, tab2 = st.tabs(["Raw Data", "Summary of Raw Data"])

        with tab1:
            with st.container():
                if res is not None:
                    df = pd.DataFrame(res.json()['data'])
                    st.dataframe(df)
                else:
                    st.markdown("Waiting for data...")

        with tab2:
            with st.container():
                if res is not None:
                    df = pd.DataFrame(res.json()['data'])
                    value_counts = df['satisfaction'].value_counts()

                    count_satisfied = value_counts.get('satisfied', 0)
                    count_neutral_dissatisfied = value_counts.get('neutral or dissatisfied', 0)

                    col1, col2 = st.columns(2)

                    col1.metric(label="Satisfied", value=f"{count_satisfied} people", delta="+ 😁")
                    col2.metric(label="Neutral or Dissatisfied", value=f"{count_neutral_dissatisfied} people", delta="- 🫤")
                else:
                    st.markdown("Waiting for data...")
