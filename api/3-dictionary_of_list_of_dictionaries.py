#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests
import sys


def record_all_tasks():
    """gather and print api data"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todo_url = f"{url}/todos"
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    counter = 0
    task_list = []
    complete_status_list = []
    username_list = []

    for item in user_data:
        username_list.append(item.get("username"))

    for item in todo_data:
        if item.get("userId") > counter:
            counter += 1
        task_list.append(item.get("title"))
        complete_status_list.append(item.get("completed"))

    todo_list = []
    for i in range(1, counter + 1):
        todo_list.append(requests.get(todo_url,
                                      params={"userId": i}).json())

    json_dict = {}
    counter = 0
    total_counter = 0
    for each in todo_list:
        json_list = []
        for i in range(len(todo_list[counter])):
            new_dict = {
                    "username": username_list[counter],
                    "task": task_list[total_counter],
                    "completed": complete_status_list[total_counter],
            }
            json_list.append(new_dict)
            total_counter += 1
        json_dict[f'{counter + 1}'] = json_list
        counter += 1

    json_object = json.dumps(json_dict)

    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)


if __name__ == "__main__":
    record_all_tasks()
