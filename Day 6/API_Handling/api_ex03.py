import requests
import json

base_url = "http://localhost:8000/tasks"

def partial_update_task(task_id):
    url = f"{base_url}/{task_id}"

    patch_data = {

        "title": "Buy groceries - 1",
        "status" : "completed"
    }
    try:
        response = requests.patch(url,json=patch_data)
        response.raise_for_status() #raise exception
        task = response.json() #data data as json file
        print(task_id)
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
if __name__ == "__main__":

    partial_update_task("task123")
    