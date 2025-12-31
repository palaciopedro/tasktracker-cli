import json
import os
import sys

def add(description):
    if len(tasks) == 0:
        task = {
            'id': 1, 
            'description': description, 
            'status': 'to do'
        }
    else:
        task = {
            'id': tasks[-1]['id'] + 1,
            'description': description,
            'status': 'to do'
        }
    tasks.append(task)


def update(id, new_description):
    for t in tasks:
        if t['id'] == int(id):
            t['description'] = new_description


def delete(id):
    for t in tasks:
        if t['id'] == int(id):
            tasks.remove(t)


def mark_in_progress(id):
    for t in tasks:
        if t['id'] == int(id):
            t['status'] = 'in progress'


def mark_done(id):
    for t in tasks:
        if t['id'] == int(id):
            t['status'] = 'done'


def list_tasks():
    for t in tasks:
        for i in t:
            print(f'{i}: {t[i]}')
        print('-' * 35)


def list_done():
    for t in tasks:
        if t['status'] == 'done':
            for i in t:
                print(f'{i}: {t[i]}')
            print('-' * 35)


def list_not_done():
    for t in tasks:
        if t['status'] != 'done':
            for i in t:
                print(f'{i}: {t[i]}')
            print('-' * 35)


def list_in_progress():
    for t in tasks:
        if t['status'] == 'in progress':
            for i in t:
                print(f'{i}: {t[i]}')
            print('-' * 35)


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)


def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
    
    with open('tasks.json', 'r') as file:
        return json.load(file)


tasks = load_tasks()

args = sys.argv

if len(args) < 2:
    exit()

command = args[1]

if command == 'add':
    add(args[2])
    save_tasks(tasks)
    print(f'Tarefa adicionada com sucesso (ID: {tasks[-1]['id']})')

elif command == 'list':
    if len(args) == 2:
        list_tasks()
    elif args[2] == 'done':
        list_done()
    elif args[2] == 'todo':
        list_not_done()
    elif args[2] == 'in-progress':
        list_in_progress()
    else:
        print(f"Comando '{command} {args[2]}' inválido!")

elif command == "update":
    update(args[2], args[3])
    save_tasks(tasks)

elif command == "delete":
    delete(args[2])
    save_tasks(tasks)

elif command == "mark-in-progress":
    mark_in_progress(args[2])
    save_tasks(tasks)

elif command == "mark-done":
    mark_done(args[2])
    save_tasks(tasks)

else:
    print(f"Comando '{command}' inválido!")
    exit()