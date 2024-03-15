#!/usr/bin/python3

"""documentation"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    URL = 'https://jsonplaceholder.typicode.com/'
    user_endpoint = f'{URL}users/{employee_id}'
    todos_endpoint = f'{URL}todos'
    
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()
    
    employee_todos = [todo for todo in todos_data if todo['userId'] == int(employee_id)]
    
    done_tasks = sum(1 for todo in employee_todos if todo['completed'])
    total_tasks = len(employee_todos)

    print(f"Employee {user_data['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in employee_todos:
        if todo['completed']:
            print(f"\t {todo['title']}")    
