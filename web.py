import streamlit as st
import functions

todos = functions.get_todo()


def add_todos():
    todo = st.session_state['new_todos']+"\n"
    todos.append(todo)
    functions.put_todos(todos)


st.title("my todo app")
st.subheader("this is my todo app")
st.write("this is testing app")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.put_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="add a new todo", on_change=add_todos, key="new_todos")

