import requests
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

reader = SimpleMFRC522()

id, text = reader.read()
print(f"Raw Data: {text}")  # Check the format of the text
