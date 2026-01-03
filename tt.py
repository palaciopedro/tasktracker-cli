import json
import os
import sys
from datetime import datetime

def add(description):
    if len(tasks) == 0:
        task = {
            'id': 1, 
            'description': description, 
            'status': 'to do',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
    else:
        task = {
            'id': tasks[-1]['id'] + 1,
            'description': description,
            'status': 'to do',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }

    tasks.append(task)




def update(id, new_description):
    for t in tasks:
        if t['id'] == int(id):
            t['description'] = new_description
            t['updatedAt'] = datetime.now().isoformat()
            


def delete(id):
    for t in tasks:
        if t['id'] == int(id):          
            tasks.remove(t)


def mark_in_progress(id):
    for t in tasks:
        if t['id'] == int(id):
            t['status'] = 'in progress'
            t['updatedAt'] = datetime.now().isoformat()
            


def mark_done(id):
    for t in tasks:
        if t['id'] == int(id):
            t['status'] = 'done'
            t['updatedAt'] = datetime.now().isoformat()
            

def print_tasks(task):
    for key in ('id', 'description', 'status'):
        print(f'{key}: {task[key]}')
    print('-' * 35)


def find_status(tasks, status):
    c = 0
    for t in tasks:
        if t['status'] == status:
            c += 1
    if c != 0:
        return True
    else:
        return False


def list_tasks():
    for t in tasks:
            print_tasks(t)


def list_done():
        for t in tasks:
            if t['status'] == 'done':
                print_tasks(t)


def list_not_done():
    c = 0
    for t in tasks:
        if t['status'] != 'done':
            c += 1
            print_tasks(t)
    if c == 0:
        print('Todas as tarefas foram finalizadas!')
        


def list_in_progress():
    for t in tasks:
        if t['status'] == 'in progress':
            print_tasks(t)


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)


def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
    
    with open('tasks.json', 'r') as file:
        return json.load(file)


def find_task(id):
    for t in tasks:
        if t['id'] == int(id):
            return True
    return False


tasks = load_tasks()

args = sys.argv

if len(args) < 2:
    exit()

command = args[1]

if command == 'add':
    if len(args) < 3:
        print('Comando inválido! Tente: add "DESCRIÇÃO"')
        exit()
    add(args[2])
    save_tasks(tasks)
    print('Tarefa adicionada com sucesso!')

elif command == 'list':
    if len(tasks) == 0:
        print('Nenhuma tarefa adicionada ainda.')
    else:
        if len(args) == 2:
            list_tasks()
        elif args[2] == 'done':
            if find_status(tasks, 'done'):
                list_done()
            else:
                print('Nenhuma tarefa finalizada ainda.')
        elif args[2] == 'todo':
            list_not_done()
        elif args[2] == 'in-progress':
            if find_status(tasks, 'in progress'):
                list_in_progress()
            else:
                print('Nenhuma tarefa em progresso ainda.')
        else:
            print(f'Comando "{command} {args[2]}" inválido! Comandos válidos list done/todo/in-progress.')

elif command == "update":
    if find_task(args[2]):
        if len(args) < 4:
            print('Comando inválido! Tente: update "ID" "NOVA DESCRIÇÃO"')
            exit()
        update(args[2], args[3])
        save_tasks(tasks)
        print('Tarefa atualizada com sucesso!')
    else:
        print('ID de tarefa não encontrado.')
        exit()

elif command == "delete":
    if find_task(args[2]):
        if len(args) < 3:
            print('Comando inválido! Tente: delete "ID"')
            exit()  
        delete(args[2])
        save_tasks(tasks)
        print('Tarefa deletada.')
    else:
        print('ID de tarefa não encontrado.')
        exit()

elif command == "mark-in-progress":
    if find_task(args[2]):
        mark_in_progress(args[2])
        save_tasks(tasks)
        print('Status da tarefa modificado para "em progresso"!')
    else:
        print('ID de tarefa não encontrado.')
        exit()


elif command == "mark-done":
    if find_task(args[2]):
        mark_done(args[2])
        save_tasks(tasks)
        print('Status da tarefa modificado para "feito"!')
    else:
        print('ID de tarefa não encontrado.')
        exit()

else:
    print(f"Comando '{command}' inválido!")
    exit()