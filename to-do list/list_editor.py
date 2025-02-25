# to_do_list = {
#     1: {
#         'task': 'Go to the gym',
#         'priority': 'high',
#         'status': 'incomplete'},
#     2: {}

to_do_list = {}

def add_task(task, priority, status):
    task_id = len(to_do_list) + 1
    to_do_list[task_id] = {
        'task': task,
        'priority': priority,
        'status': status
    }
    return to_do_list

def edit_task(task_id, task, priority, status):
    to_do_list[task_id] = {
        'task': task,
        'priority': priority,
        'status': status
    }
    return to_do_list

def delete_task(task_id):
    del to_do_list[task_id]
    return to_do_list

def view_all_tasks():
    return to_do_list