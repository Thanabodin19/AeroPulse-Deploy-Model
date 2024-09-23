from typing import Counter
import streamlit as st
import pandas as pd
import requests
from sklearn.inspection import permutation_importance
import gspread
from google.oauth2.service_account import Credentials
from typing import Union
from fastapi import FastAPI
import joblib
import pandas as pd
import pickle

path_production = "/app/pipelines/"

def transform_pipeline_ecoPlus(df):
    df = df.drop(["id"], axis=1)
    print(df)
    encoder = pickle.load(open(f"{path_production}encoder_ecoPlus.pkl", 'rb'))
    # encoder = joblib.load('../../pipelines/encoder_business.pkl')
    model = pickle.load(open(f"{path_production}model_LR_ecoPlus.pkl", 'rb'))
    scaler = pickle.load(open(f"{path_production}scaler_LR_ecoPlus.pkl", 'rb'))
    
    all_encoded = ['Inflight wifi service', 
                    'Ease of Online booking', 
                    'Food and drink', 'Online boarding', 
                    'Seat comfort', 'Inflight entertainment', 
                    'On-board service', 'Leg room service', 
                    'Baggage handling', 'Checkin service', 
                    'Inflight service', 'Cleanliness', 
                    'Customer Type', 'Type of Travel', 'Class']
    encoded = encoder.fit_transform(df[all_encoded])

    df_encoded = pd.DataFrame(encoded.toarray(), 
                            columns=encoder.get_feature_names_out(all_encoded))
    # # encoding
    df_encoded = df_encoded.astype(int)
    print(df_encoded.shape)
    
    # print(len(list(df_encoded)))
    # df_encoded = df_encoded[6:]
    df_drop_dummy = df[6:].drop(all_encoded, axis=1)
    
    df_drop_dummy = df_drop_dummy.drop(["Gender", "Gate location", "Arrival Delay in Minutes", "Departure/Arrival time Convenient"], axis=1)
    print(df_drop_dummy.shape)
    df_drop_dummy_reset = df_drop_dummy.reset_index(drop=True)
    df_encoded_reset = df_encoded.reset_index(drop=True)

    df_final = pd.concat([df_encoded_reset, df_drop_dummy_reset], axis=1)
    
    # standardization
    df_scaler = scaler.transform(df_final.iloc[:-6])
    preds = model.predict(df_scaler)
    
    feature_importance = pd.DataFrame({
        'Feature': df_final.columns.tolist(),  # List of feature names
        'Importance': model.coef_[0]  # Coefficients of the logistic regression model
    }).sort_values(by='Importance', ascending=False)
    
    return preds, feature_importance

def transform_pipeline_eco(df):
    df = df.drop(["id"], axis=1)
    print(df)
    encoder = pickle.load(open(f"{path_production}encoder_eco.pkl", 'rb'))
    # encoder = joblib.load('../../pipelines/encoder_business.pkl')
    model = pickle.load(open(f"{path_production}model_LR_eco.pkl", 'rb'))
    scaler = pickle.load(open(f"{path_production}scaler_LR_eco.pkl", 'rb'))
    
    all_encoded = ['Inflight wifi service', 
                    'Ease of Online booking', 
                    'Food and drink', 'Online boarding', 
                    'Seat comfort', 'Inflight entertainment', 
                    'On-board service', 'Leg room service', 
                    'Baggage handling', 'Checkin service', 
                    'Inflight service', 'Cleanliness', 
                    'Customer Type', 'Type of Travel', 'Class']
    encoded = encoder.fit_transform(df[all_encoded])

    df_encoded = pd.DataFrame(encoded.toarray(), 
                            columns=encoder.get_feature_names_out(all_encoded))
    # # encoding
    df_encoded = df_encoded.astype(int)
    print(df_encoded.shape)
    
    # print(len(list(df_encoded)))
    # df_encoded = df_encoded[6:]
    df_drop_dummy = df[6:].drop(all_encoded, axis=1)
    
    df_drop_dummy = df_drop_dummy.drop(["Gender", "Gate location", "Arrival Delay in Minutes", "Departure/Arrival time Convenient"], axis=1)
    print(df_drop_dummy.shape)
    df_drop_dummy_reset = df_drop_dummy.reset_index(drop=True)
    df_encoded_reset = df_encoded.reset_index(drop=True)

    df_final = pd.concat([df_encoded_reset, df_drop_dummy_reset], axis=1)
    
    # standardization
    df_scaler = scaler.transform(df_final.iloc[:-6])
    preds = model.predict(df_scaler)
    
    feature_importance = pd.DataFrame({
        'Feature': df_final.columns.tolist(),  # List of feature names
        'Importance': model.coef_[0]  # Coefficients of the logistic regression model
    }).sort_values(by='Importance', ascending=False)
    
    return preds, feature_importance

def transform_pipeline_business(df):
    df = df.drop(["id"], axis=1)
    print(df)
    encoder = pickle.load(open(f"{path_production}encoder_business.pkl", 'rb'))
    # encoder = joblib.load('../../pipelines/encoder_business.pkl')
    model = pickle.load(open(f"{path_production}model_LR_business.pkl", 'rb'))
    scaler = pickle.load(open(f"{path_production}scaler_LR_business.pkl", 'rb'))
    
    all_encoded = ['Inflight wifi service', 
                    'Ease of Online booking', 
                    'Food and drink', 'Online boarding', 
                    'Seat comfort', 'Inflight entertainment', 
                    'On-board service', 'Leg room service', 
                    'Baggage handling', 'Checkin service', 
                    'Inflight service', 'Cleanliness', 
                    'Customer Type', 'Type of Travel', 'Class']
    encoded = encoder.fit_transform(df[all_encoded])

    df_encoded = pd.DataFrame(encoded.toarray(), 
                            columns=encoder.get_feature_names_out(all_encoded))
    # # encoding
    df_encoded = df_encoded.astype(int)
    print(df_encoded.shape)
    # print(len(list(df_encoded)))
    # df_encoded = df_encoded[6:]
    df_drop_dummy = df[6:].drop(all_encoded, axis=1)
    
    df_drop_dummy = df_drop_dummy.drop(["Gender", "Gate location", "Arrival Delay in Minutes", "Departure/Arrival time Convenient"], axis=1)
    print(df_drop_dummy.shape)
    df_drop_dummy_reset = df_drop_dummy.reset_index(drop=True)
    df_encoded_reset = df_encoded.reset_index(drop=True)

    df_final = pd.concat([df_encoded_reset, df_drop_dummy_reset], axis=1)
    print(df_final.shape)
    
    # standardization
    df_scaler = scaler.transform(df_final.iloc[:-6])
    preds = model.predict(df_scaler)
    
    feature_importance = pd.DataFrame({
        'Feature': df_final.columns.tolist(),  # List of feature names
        'Importance': model.coef_[0]  # Coefficients of the logistic regression model
    }).sort_values(by='Importance', ascending=False)
    
    return preds, feature_importance

def get_ecoPlus_summary():
    file_path = "/app/backend/AeroPulse_Passenger_Data.xlsx"

    # Read a specific sheet by name
    df = pd.read_excel(file_path, sheet_name="sheet3")
    data = df.to_dict(orient='records')
    preds, feature_importance = transform_pipeline_ecoPlus(df)
    # # Convert to a dictionary (records orientation)
    feature_importance_records = feature_importance.to_dict(orient='records')

    # # Return the data as JSON response
    return {"data": data[6:], "preds": preds.tolist(), "feature_importance": feature_importance_records}

def get_eco_summary():
    file_path = "/app/backend/AeroPulse_Passenger_Data.xlsx"

    # Read a specific sheet by name
    df = pd.read_excel(file_path, sheet_name="sheet2")
    data = df.to_dict(orient='records')
    preds, feature_importance = transform_pipeline_eco(df)
    # # Convert to a dictionary (records orientation)
    feature_importance_records = feature_importance.to_dict(orient='records')

    # # Return the data as JSON response
    return {"data": data[6:], "preds": preds.tolist(), "feature_importance": feature_importance_records}

def get_business_summary():    
    # Specify the path to the Excel file
    file_path = "/app/backend/AeroPulse_Passenger_Data.xlsx"

    # Read a specific sheet by name
    df = pd.read_excel(file_path, sheet_name="sheet1")
    data = df.to_dict(orient='records')
    
    preds, feature_importance = transform_pipeline_business(df)
    # Convert to a dictionary (records orientation)
    feature_importance_records = feature_importance.to_dict(orient='records')

    # Return the data as JSON response
    return {"data": data[6:], "preds": preds.tolist(), "feature_importance": feature_importance_records}

if __name__ == "__main__":
    
    st.set_page_config(layout='wide', page_title="AeroPulse Visualization", page_icon="✈️")
    
    # Create a container
    with st.container():
        # Create two columns
        col1, col2 = st.columns([6, 1])  # Adjust the width ratio to create space between the columns
        with col1:
            st.title("AeroPulse ✈️")
        with col2:
            option = st.selectbox(
                "Analyzer",
                ("None", "Economy Class", "Economy Plus Class", "Business Class"),
            )
    st.markdown("**- Classify Satisfaction, Neutral or Dissatisfaction of passenger based on history data -**")

    if option == "Economy Class":
        res = get_eco_summary()
    elif option == "Economy Plus Class":
        res = get_ecoPlus_summary()
    elif option == "Business Class":
        res = get_business_summary()
    else:
        res = None

    with st.container(border=True):
        if res != None:
            st.markdown("<h3 style='margin-top: 20px; margin-bottom: 70px; text-align: center;'>CDTI Airplane Flight 640</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            if res != None:
                st.image("/app/frontend/AirplaneSeat.png")
            # st.write("Airplan IMG")
        with col2:
            with st.container():
                if res != None:
                    st.success('Analyze succesfully', icon="✅")
                    if option == "Economy Class":
                        st.markdown("### :green[Economy Class]")
                    elif option == "Economy Plus Class":
                        st.markdown("### :blue[Economy Plus Class]")
                    elif option == "Business Class":
                        st.markdown("### :rainbow[Business Class]")
                    df = pd.DataFrame(res['data'])
                    preds = res['preds']
                    feature_importance = res['feature_importance']
                    
                    df_preds = pd.DataFrame(preds)
                    satisfaction_counts = df_preds.value_counts()
                    count_satisfied = satisfaction_counts['satisfied']
                    count_neutral_dissatisfied = satisfaction_counts['neutral or dissatisfied']
                    
                    sa_col1, dis_col2 = st.columns(2)
                    
                    sa_col1.metric(label="Satisfied", value=f"{count_satisfied} 👤", delta="+ 😁")
                    dis_col2.metric(label="Neutral or Dissatisfied", value=f"{count_neutral_dissatisfied} 👤", delta="- 🫤")
                    
                    # Extracting the features with negative importance from the nested structure
                    negative_features = [item['Feature'] for item in feature_importance if item['Importance'] < 0]
                    
                    # Extract base names (ignore numbers after the underscore)
                    base_names = [name.split('_')[0] for name in negative_features]

                    # Count occurrences of base names
                    name_counts = Counter(base_names)
                    print(name_counts)
                    
                    # Get names that appear exactly once
                    unique_names = [name for name, count in name_counts.items() if count > 1]
                    
                    with st.container(border=True):
                        st.markdown("#### Services that need to be developed to enhance passenger satisfaction. 📖")
                        
                        for name in unique_names[0:3]:
                            st.markdown(f"""
                                        - {name}
                                        """)
                        
                    st.markdown("> based on history data")
        
                    st.markdown("<h3 style='margin-bottom: 20px; text-align: center;'></h3>", unsafe_allow_html=True)
    
    tab1 = st.tabs(["View Raw Data"])
    
    with tab1:
        with st.container():
            if res != None:
                df = pd.DataFrame(res['data'])
                st.dataframe(df) 
            else:
                st.markdown("Waiting for data...")