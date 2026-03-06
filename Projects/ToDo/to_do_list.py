import pandas as pd
import streamlit as st

# File path for CSV
filepath = "To_Do.csv"

# Try to read the CSV, if it doesn't exist create a new dataframe
try:
    df = pd.read_csv(filepath)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Task", "Days_Due_In"])

# Streamlit App
st.title("To-Do List")

# Show current tasks
st.subheader("Current Tasks")
st.dataframe(df)

# Section to add a new task
st.subheader("Add A Task")
task = st.text_input("Task Name")
due = st.text_input("Days Due In")

# Button to add task
if st.button("Add Task"):
    if task and due.isdigit():  # Ensure input is valid
        new_row = pd.DataFrame({"Task": [task], "Days_Due_In": [int(due)]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(filepath, index=False)
        st.success("Task added!")
    else:
        st.error("Enter a task name and a number for Days Due In.")