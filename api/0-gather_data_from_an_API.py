#!/usr/bin/python3
"""
Uses API to return info on given employee's progress
"""


if __name__ == "__main__":
    import requests
    import sys

    def employee_to_do_progress(employee_id):
        """
        method for getting data from api
        """
        api_url = 'https://jsonplaceholder.typicode.com/'

        employee_request = requests.get(f'{api_url}users/{employee_id}')
        employee_data = employee_request.json()
        employee_name = employee_data.get('name')

        todo_request = requests.get(f'{api_url}todos?userId={employee_id}')
        todo_data = todo_request.json()
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, completed_tasks, total_tasks))
        for task in todo_data:
            if task['completed']:
                print(f"\t {task['title']}")

    employee_id = sys.argv[1]
    employee_to_do_progress(employee_id)
