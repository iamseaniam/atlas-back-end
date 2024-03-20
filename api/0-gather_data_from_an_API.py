#!/usr/bin/python3
""" returns information about to-do list progress """
import requests
import sys


def gather_api_data():
    """gather and print api data"""
    if(len(sys.argv) != 2):
        print("Error not 3 commands")

    employee_id = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": employee_id}).json()
    EMPLOYEE_NAME = user_data.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    completed_tasks = []

    for item in todo_data:
        TOTAL_NUMBER_OF_TASKS += 1
        if item.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            completed_tasks.append(item.get("title"))

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    gather_api_data()
