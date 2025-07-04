import requests
import json
import pandas as pd
import datetime
import time
import schedule

API_URL = "http://api.open-notify.org/iss-now.json"

REPORT_FILE = "iss_location_report.csv"

def fetch_iss_location():
    try:
        response = requests.get(API_URL)
        response.raise_for_status() #raise exception
        data = response.json() #data data as json file
       
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return  None


def generate_report_entry():
    iss_data = fetch_iss_location()

    if iss_data:
        timestamp = datetime.datetime.fromtimestamp(iss_data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']

        print(f"Timestamp: {timestamp} | Latitude: {latitude} | Longitude: {longitude}")
    
       

# Call the function 5 times and store the results
data_list = []
""""
for iter in range(5):
    iter = generate_report_entry()
    data_list.append(iter)
    time.sleep(1)  # optional: wait 1 second between calls to get slightly different data
    
    print(f"{data_list}") # Print the collected data """

for i in range(5):
    entry = generate_report_entry()
    if entry:
        data_list.append(entry)
    time.sleep(1)
    
    print(data_list)