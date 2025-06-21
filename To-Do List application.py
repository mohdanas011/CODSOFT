import tkinter as tk
from tkinter import messagebox, filedialog

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            tasks = tasks_listbox.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        tasks_listbox.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                tasks_listbox.insert(tk.END, line.strip())

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)

# Entry
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack()

# Task List
tasks_listbox = tk.Listbox(root, font=("Arial", 14), height=15, width=30)
tasks_listbox.pack(pady=10)

# Buttons
delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", width=20, command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", width=20, command=load_tasks)
load_button.pack(pady=5)

# Run the app
root.mainloop()
