import streamlit as st
import pandas as pd
from io import BytesIO
import base64
import time

# Function to download data as an Excel file
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

def load_data():
    try:
        return pd.read_csv('rfid_data.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['RFID', 'Bin No.', 'Location Rack', 'Part No.', 'Name'])

st.title('Dashboard | Inventory')

# Initialize or load session state
if 'rfid_data' not in st.session_state:
    st.session_state['rfid_data'] = load_data()

# Display the data in the app
st.dataframe(st.session_state['rfid_data'])

# Button to refresh data
if st.button('Refresh Data'):
    st.session_state['rfid_data'] = load_data()

# Button to export data
if st.button('Export Data as Excel'):
    val = to_excel(st.session_state['rfid_data'])
    b64 = base64.b64encode(val).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="rfid_data.xlsx">Download Excel file</a>'
    st.markdown(href, unsafe_allow_html=True)
