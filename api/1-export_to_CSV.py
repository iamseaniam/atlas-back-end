#!/usr/bin/python3
"""
Uses API to return info on given employee's progress
"""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    def employee_to_do_progress_cvs_export(employee_id):
        """
        method for getting exporting to a cvs data from api
        """
        # define api url
        api_url = 'https://jsonplaceholder.typicode.com/'

        # use get to get employee data
        employee_request = requests.get(f'{api_url}users/{employee_id}')
        # jsonise to get data
        employee_data = employee_request.json()
        # get emplyee info
        employee_name = employee_data.get('username')

        # get todo list
        todo_request = requests.get(f'{api_url}todos?userId={employee_id}')
        # get data
        todo_data = todo_request.json()
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)
        # create list for data to export
        csv_data = []
        # create csv file name
        csv_file_name = f'{employee_id}.csv'

        # add tasks to csv data
        for task in todo_data:
            if task['completed']:
                title = task.get('title')
                data_to_add = [f"{employee_id}", f"{employee_name}",
                               "True", f"{title}"]
                csv_data.append(data_to_add)
            else:
                title = task.get('title')
                data_to_add = [f"{employee_id}", f"{employee_name}",
                               "False", f"{title}"]
                csv_data.append(data_to_add)

        # open file and write data
        with open(csv_file_name, 'w', newline='') as file:
            # Create a CSV writer object
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            # Write the data to the CSV file
            csv_writer.writerows(csv_data)

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]
    # Call the function to get and display employee TODO list progress
    employee_to_do_progress_cvs_export(employee_id)
