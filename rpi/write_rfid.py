import csv
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

reader = SimpleMFRC522()

try:
    with open('BIN-DATA.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # Assign each piece of data to its respective variable
            rack_no = row['Bin NO']
            bin_no = row['Location Rack']
            part_no = row['Part No']
            name = row['Name']

            # Concatenate the data into a comma-separated string
            data_to_write = f"{rack_no},{bin_no},{part_no},{name}"
            print(f"Writing the following data to a tag: {data_to_write}")
            
            # Wait for an RFID tag to be presented
            print("Please present an RFID tag to write.")
            
            # Write the data to the RFID tag
            reader.write(data_to_write)
            
            print("Data written successfully. Please present the next tag.")
            time.sleep(2)  # Short delay before the next write

finally:
    GPIO.cleanup()

