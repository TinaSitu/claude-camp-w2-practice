"""
Exercise 3: Todo List with File Saving
A command-line todo list manager that saves tasks to a local
JSON file so data is preserved after the program closes.

Key concepts:
- Reading and writing JSON files
- Exception handling for missing files
- List and dictionary data structures
- Data persistence across program restarts
"""

import json
import os


# ─────────────────────────────────────────
# CONSTANTS
# Define the filename where todos will be saved
# ─────────────────────────────────────────
TODO_FILE = "todos.json"


# ─────────────────────────────────────────
# FILE OPERATION: Load todos from JSON file
# If file does not exist, return empty list (no crash)
# If file is corrupted, return empty list (no crash)
# ─────────────────────────────────────────
def load_todos():
    # Check if the file exists before trying to open it
    if not os.path.exists(TODO_FILE):
        # File not found — this is normal on first run, just return empty list
        return []

    try:
        # Open and read the JSON file
        with open(TODO_FILE, "r") as file:
            todos = json.load(file)
            return todos
    except (json.JSONDecodeError, ValueError):
        # File exists but content is corrupted or invalid JSON
        print("  [!] Warning: todo file was corrupted. Starting fresh.")
        return []


# ─────────────────────────────────────────
# FILE OPERATION: Save todos to JSON file
# Overwrites the file with the latest todo list
# ─────────────────────────────────────────
def save_todos(todos):
    try:
        # Write the todo list to the JSON file
        # indent=2 makes the file human-readable
        with open(TODO_FILE, "w") as file:
            json.dump(todos, file, indent=2)
    except IOError:
        # Could not write to file (e.g. permission error)
        print("  [!] Error: could not save todos to file.")


# ─────────────────────────────────────────
# OPERATION 1: Add a new todo item
# ─────────────────────────────────────────
def add_todo(todos):
    # Get the task description from the user
    while True:
        task = input("  Enter task description: ").strip()
        if task:
            break
        print("  [!] Task cannot be empty. Please try again.")

    # Build the todo item as a dictionary
    # done = False means the task is not completed yet
    todo = {
        "id": len(todos) + 1,
        "task": task,
        "done": False,
    }

    # Add to the list and save immediately
    todos.append(todo)
    save_todos(todos)
    print(f"  [OK] Task added: '{task}'")


# ─────────────────────────────────────────
# OPERATION 2: Mark a todo item as complete
# ─────────────────────────────────────────
def complete_todo(todos):
    # Cannot complete anything if list is empty
    if not todos:
        print("  [!] No tasks found. Add some tasks first.")
        return

    # Show the list so user knows which ID to pick
    view_todos(todos)

    while True:
        try:
            task_id = int(input("  Enter task ID to mark as complete: ").strip())

            # Find the matching todo by its ID
            todo = next((t for t in todos if t["id"] == task_id), None)

            if todo is None:
                print(f"  [!] No task found with ID {task_id}. Please try again.")
                continue

            if todo["done"]:
                # Task is already marked as done
                print(f"  [!] Task {task_id} is already completed.")
                break

            # Mark as done and save
            todo["done"] = True
            save_todos(todos)
            print(f"  [OK] Task {task_id} marked as complete: '{todo['task']}'")
            break

        except ValueError:
            # User typed something that is not a number
            print("  [!] Invalid input. Please enter a valid task ID number.")


# ─────────────────────────────────────────
# OPERATION 3: Delete a todo item
# ─────────────────────────────────────────
def delete_todo(todos):
    # Cannot delete anything if list is empty
    if not todos:
        print("  [!] No tasks found. Nothing to delete.")
        return

    # Show the list so user knows which ID to pick
    view_todos(todos)

    while True:
        try:
            task_id = int(input("  Enter task ID to delete: ").strip())

            # Find the matching todo by its ID
            todo = next((t for t in todos if t["id"] == task_id), None)

            if todo is None:
                print(f"  [!] No task found with ID {task_id}. Please try again.")
                continue

            # Remove from list and save
            todos.remove(todo)
            save_todos(todos)
            print(f"  [OK] Task {task_id} deleted: '{todo['task']}'")
            break

        except ValueError:
            # User typed something that is not a number
            print("  [!] Invalid input. Please enter a valid task ID number.")


# ─────────────────────────────────────────
# OPERATION 4: View all todo items
# Shows pending tasks first, then completed ones
# ─────────────────────────────────────────
def view_todos(todos):
    if not todos:
        print("\n  (Your todo list is empty.)")
        return

    # Count pending and completed tasks for the summary
    pending   = [t for t in todos if not t["done"]]
    completed = [t for t in todos if t["done"]]

    print(f"\n  {'─' * 42}")
    print(f"  {'ID':<6} {'Status':<12} Task")
    print(f"  {'─' * 42}")

    # Print pending tasks first
    for todo in pending:
        status = "[ ] Pending"
        print(f"  {todo['id']:<6} {status:<12} {todo['task']}")

    # Print completed tasks below
    for todo in completed:
        status = "[x] Done"
        print(f"  {todo['id']:<6} {status:<12} {todo['task']}")

    # Print summary footer
    print(f"  {'─' * 42}")
    print(f"  Pending: {len(pending)}   Completed: {len(completed)}   Total: {len(todos)}")
    print(f"  {'─' * 42}")


# ─────────────────────────────────────────
# MENU: Display options to the user
# ─────────────────────────────────────────
def show_menu():
    print("\n" + "=" * 42)
    print("    Todo List Manager")
    print("=" * 42)
    print("  1. Add a task")
    print("  2. Mark a task as complete")
    print("  3. Delete a task")
    print("  4. View all tasks")
    print("  0. Exit")
    print("=" * 42)


# ─────────────────────────────────────────
# MAIN FUNCTION: Program entry point
# Loads existing todos on startup, then runs
# the menu loop until the user exits
# ─────────────────────────────────────────
def main():
    print("Welcome to the Todo List Manager!")

    # Load existing todos from file on startup
    # If no file exists yet, todos will be an empty list
    todos = load_todos()

    if todos:
        print(f"  [OK] Loaded {len(todos)} task(s) from previous session.")
    else:
        print("  [OK] Starting with a fresh todo list.")

    while True:
        show_menu()

        try:
            choice = input("  Enter your choice (0-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  Goodbye!")
            break

        if choice == "1":
            print("\n  -- Add Task --")
            add_todo(todos)

        elif choice == "2":
            print("\n  -- Complete Task --")
            complete_todo(todos)

        elif choice == "3":
            print("\n  -- Delete Task --")
            delete_todo(todos)

        elif choice == "4":
            print("\n  -- All Tasks --")
            view_todos(todos)

        elif choice == "0":
            print("\n  Goodbye!")
            break

        else:
            print("  [!] Invalid choice. Please enter a number between 0 and 4.")


# ─────────────────────────────────────────
# Run only when executed directly
# (not when imported as a module)
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()