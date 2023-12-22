import requests
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

reader = SimpleMFRC522()

# Initialize last_id and last_read_time
last_id = None
last_read_time = 0
read_delay = 2  # Delay in seconds to avoid immediate re-reads

try:
    while True:
        current_time = time.time()
        id, text = reader.read()

        # Check if the tag is different from the last, or sufficient time has passed
        if id != last_id or (current_time - last_read_time) > read_delay:
            last_id = id
            last_read_time = current_time

            parts = text.split(',')  # Assuming tab-separated values
            if len(parts) >= 4:
                # Extract values assuming each part is in 'key: value' format
                rack_no = parts[0].split(': ')
                bin_no = parts[1].split(': ')
                name = parts[2].split(': ')
                part_no = parts[3].split(': ')

                data = {
                    'RFID': id,
                    'Bin No.': bin_no,
                    'Location Rack': rack_no,
                    'Part No.': part_no,
                    'Name': name
                }
                # Send data to your server where the Flask app is running
                requests.post('http://192.168.0.104:5000/update_rfid', json=data)
                print(f"Tag {id} read and data sent.")

        time.sleep(0.5)  # Brief sleep to reduce CPU usage, adjust as needed
finally:
    GPIO.cleanup()

