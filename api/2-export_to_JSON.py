import requests
import json

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee details
    employee_response = requests.get(employee_endpoint)
    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetch TODO list
    todo_response = requests.get(todo_endpoint)
    todo_data = todo_response.json()

    # Create a dictionary to store the JSON data
    employee_json = {
        "USER_ID": []
    }

    # Populate the dictionary with TODO list data
    for task in todo_data:
        task_json = {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        employee_json["USER_ID"].append(task_json)

    # Create a JSON file for the employee
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(employee_json, json_file, indent=4)

    print(f"Data exported to {json_filename}")

# Input employee ID as an integer
employee_id = int(input("Enter Employee ID: "))
get_employee_todo_progress(employee_id)
