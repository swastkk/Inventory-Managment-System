import streamlit as st
import pandas as pd
from io import BytesIO
import base64
import time

# Function to load the latest RFID scan data
def load_latest_data():
    try:
        return pd.read_csv('rfid_data.csv')
    except FileNotFoundError:
        return pd.DataFrame({'RFID': [], 'Bin No.': [], 'Location Rack': [], 'Part No.': [], 'Name': []})

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

def main():
    st.title('Inventory Dashboard')

    data_placeholder = st.empty()

    if 'rfid_data' not in st.session_state:
        st.session_state['rfid_data'] = load_latest_data()

    # Button to export data
    if st.button('Export Data as Excel'):
        val = to_excel(st.session_state['rfid_data'])
        b64 = base64.b64encode(val).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="rfid_data.xlsx">Download Excel file</a>'
        st.markdown(href, unsafe_allow_html=True)

    while True:
        # Load and display the latest data
        st.session_state['rfid_data'] = load_latest_data()
        data_placeholder.dataframe(st.session_state['rfid_data'])

        # Wait some time before the next check
        time.sleep(1)

if __name__ == '__main__':
    main()
