import functions
import FreeSimpleGUI as Sm
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt","w") as file:
        pass
Sm.theme("LightBlue7")
clock = Sm.Text("clock", key="clock")
label = Sm.Text("Type a To-Do")
inputbox = Sm.InputText(tooltip="enter todo", key="todo")
add = Sm.Button("add")
list_item = Sm.Listbox(values=functions.get_todo(), key="task",
                       size=[45, 10], enable_events=True)

edit = Sm.Button("Edit")
complete = Sm.Button("complete")
leave = Sm.Button("exit")
layout = [[clock], [label], [inputbox, add], [list_item, edit, complete], [leave]]
window = Sm.Window('My ToDo APP',
                   layout=layout,
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.put_todos(todos)
            window['task'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todos_to_edit = values.get("task")
                new_todo = values.get('todo', '').strip()
                todos = functions.get_todo()
                index = todos.index(todos_to_edit[0])
                todos[index] = new_todo + "\n"
                functions.put_todos(todos)
                window['task'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                Sm.popup("Please select a task to edit", font=("Helvetica", 20))

        case "complete":
            try:
                todo_to_complete = values["task"][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.put_todos(todos)
                window['task'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                Sm.popup("Please select the task to Complete", font=("Helvetica", 20))
        case 'task':
            window['todo'].update(value=values['task'][0])
        case "exit":
            break
        case Sm.WIN_CLOSED:
            break
window.close()
