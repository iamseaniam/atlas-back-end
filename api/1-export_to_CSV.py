#!/usr/bin/python3
"""extend your script to export data in CSV"""
import csv
import requests
import sys


def export_to_csv():
    """gather and print api data"""
    if(len(sys.argv) != 2):
        print("Error not 3 commands")

    USER_ID = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(USER_ID)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": USER_ID}).json()
    EMPLOYEE_UN = user_data.get("username")
    EMPLOYEE_NAME = user_data.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    completed_tasks = []

    for item in todo_data:
        TOTAL_NUMBER_OF_TASKS += 1
        if item.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            completed_tasks.append(item.get("title"))

    with open('{}.csv'.format(USER_ID), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in todo_data:
            writer.writerow((USER_ID, EMPLOYEE_UN,
                            item.get("completed"), item.get("title")))

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    export_to_csv()
