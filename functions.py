filep = "todo.txt"


def get_todo(filepath=filep):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def put_todos(todos_arg, filepath=filep):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("this is the function")
    print(get_todo())
