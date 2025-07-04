import requests
import json

base_url = "http://localhost:8000/tasks"

#def get_tasks_by_status(status):
    #print(f" getting tasks with status : '{status}")

def fetch_iss_location():
    try:
        response = requests.get(base_url)
        response.raise_for_status() #raise exception
        data = response.json() #data data as json file
        
        print (json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return  None   

#fetch_iss_location()

def get_specific_task(task_id):
    url = f"{base_url}/{task_id}"

    try:
        response = requests.get(url)
        response.raise_for_status() #raise exception
        task = response.json() #data data as json file
        
        print (json.dumps(task, indent=2))
        return task
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error :  {task_id} NOT FOUND")
        else:
            print(f"Error FETCHING TASK :  {task_id}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from : {task_id}")
        return  None 

get_specific_task("task456")
get_specific_task("task123")