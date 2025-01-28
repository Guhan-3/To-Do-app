from functions import get_todo
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)
while True:
    todo = input("enter add or show or break or complete:")
    todo.strip()
    if todo.startswith("add"):
        task = todo[4:]
        todos = get_todo()
        todos.append(task + '\n')
        functions.put_todos(todos)
    elif todo.startswith("show"):
        todos = get_todo("todo.txt")
        # new_todos=[item.strip("\n") for item in todos]
        for i, item in enumerate(todos, 1):
            item = item.strip('\n')
            show = f"{i}-{item}"
            print(show)
    elif todo.startswith("edit"):
        try:
            number = int(todo[5:])
            number = number - 1
            todos = get_todo()
            new = input("enter the new task:")
            todos[number] = new + '\n'
            functions.put_todos(todos)
        except ValueError:
            print("Please Enter a Valid Command")
            continue

    elif todo.startswith("complete"):
        try:
            number = int(todo[9:])
            todos = get_todo()
            index = number - 1
            remove = todos[index].strip('\n')
            todos.pop(index)
            functions.put_todos(todos)
            msg = f"The completed task is {remove}"
            print(msg)
        except IndexError:
            print("enter a Valid Number")
            continue

    elif todo.startswith("exit"):
        break
    else:
        print("command is not valid")
print("this is a apps")
