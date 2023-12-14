from flask import Flask, request
import pandas as pd
import os

app = Flask(__name__)

file_path = 'rfid_data.csv'
columns = ['RFID', 'Bin No.', 'Location Rack', 'Part No.', 'Name']

@app.route('/update_rfid', methods=['POST'])
def update_rfid():
    data = request.json
    df = pd.DataFrame(data, columns=columns)

    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode='a', index=False, header=True)
    else:
        df.to_csv(file_path, mode='a', index=False, header=False)
    
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)