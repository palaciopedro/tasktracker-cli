tasks = []

def add(description):
    task = {
        'id': len(tasks) + 1, 
        'description': description, 
        'status': 'to do'
    }

    tasks.append(task)


def update(id, new_description):
    for t in tasks:
        if t['id'] == id:
            t['description'] = new_description


def delete(id):
    for t in tasks:
        if t['id'] == id:
            tasks.remove(t)


def mark(status, id):
    for t in tasks:
        if t['id'] == id:
            t['status'] = status


def list():
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


def list_notdone():
    for t in tasks:
        if t['status'] != 'done':
            for i in t:
                print(f'{i}: {t[i]}')
            print('-' * 35)


def list_inprogress():
    for t in tasks:
        if t['status'] == 'in progress':
            for i in t:
                print(f'{i}: {t[i]}')
            print('-' * 35)


add('lavar louça')
add('cozinhar macarrao')
add('estudar')
update(1, 'lavar e secar louça')
mark('done', 3)
add('correr')
mark('done', 4)
add('corinthians')
mark('in progress', 5)
delete(5)

list_inprogress()