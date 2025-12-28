tasks = []

def add(description):
    task = {'id': len(tasks) + 1, 'description': description, 'status': 'in progress'}

    tasks.append(task)


def update(id, new_description):
    tasks[id - 1]['description'] = new_description


def delete(id):
    tasks.pop(id - 1)
    for i, e in enumerate(tasks):
        e['id'] = i + 1


def list():
    print(tasks)

add('lavar louça')
add('cozinhar macarrao')
add('estudar')
update(1, 'lavar e secar louça')
delete(2)

list()