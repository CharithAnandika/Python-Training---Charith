import requests
import json

base_url = "http://localhost:8000/tasks"

def create_new_task():
    new_task_data = {
    "title": "Buy Phones",
    "description": "samsung, iphone, pixel, huawei",
    "status": "pending",
    "dueDate": "2025-06-21"
}
    try:
        response = requests.post(base_url,json=new_task_data)
        response.raise_for_status() #raise exception
        data = response.json() #data data as json file
        
        print (json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return  None 

create_new_task()