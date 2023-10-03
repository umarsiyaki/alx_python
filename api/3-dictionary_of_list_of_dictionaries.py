import requests
import json

def get_all_employees_todo_progress():
    # Define the API endpoint to fetch all users
    users_endpoint = "https://jsonplaceholder.typicode.com/users"
    
    # Fetch all users
    users_response = requests.get(users_endpoint)
    users_data = users_response.json()
    
    # Create a dictionary to store the JSON data
    all_employees_json = {}
    
    # Iterate through each employee
    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        
        # Define the API endpoint for the user's TODO list
        todo_endpoint = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        
        # Fetch the user's TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()
        
        # Create a list to store the user's tasks
        tasks_list = []
        
        # Populate the list with TODO list data for this user
        for task in todo_data:
            task_json = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            tasks_list.append(task_json)
        
        # Add the tasks list to the JSON dictionary
        all_employees_json[user_id] = tasks_list

    # Create a JSON file for all employees
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_json, json_file, indent=4)

    print(f"Data exported to {json_filename}")

# Call the function to export data for all employees
get_all_employees_todo_progress()
