import requests

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee details
    employee_response = requests.get(employee_endpoint)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetch TODO list
    todo_response = requests.get(todo_endpoint)
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

# Input employee ID as an integer
employee_id = int(input("Enter Employee ID: "))
get_employee_todo_progress(employee_id)
