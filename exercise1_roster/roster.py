"""
Exercise 1: Supplier Roster Manager
Stores supplier information using a Python dictionary.
Supports: add, search, delete, list — with full input validation.
"""

from datetime import date
import re 


# ─────────────────────────────────────────
# DATA STORE
# We use a dictionary to hold all suppliers.
# Key   = supplier name (string)
# Value = another dictionary with email and join_date
# Example: {"Apple Inc": {"email": "apple@mail.com", "join_date": "2024-01-15"}}
# ─────────────────────────────────────────
roster = {}


# ─────────────────────────────────────────
# OPERATION 1: ADD a new supplier
# ─────────────────────────────────────────
def add_supplier(name, email, join_date):

    # Check 1: Warn if the exact same name already exists
    if name in roster:
        print(f"  [Warning] Supplier name '{name}' already exists in the roster.")
        print(f"  [Warning] Adding anyway with a duplicate name.")

    # Check 2: Warn if the same email is already used by another supplier
    for existing_name, info in roster.items():
        if info["email"] == email:
            print(f"  [Warning] Email '{email}' is already used by '{existing_name}'.")
            print(f"  [Warning] Adding anyway with a duplicate email.")
            break  # Only warn once even if email appears multiple times

    # Save the supplier regardless of warnings
    # If name already exists, this overwrites the old entry with the new one
    roster[name] = {
        "email": email,
        "join_date": join_date,
    }
    print(f"  [OK] Supplier '{name}' added successfully.")


# ─────────────────────────────────────────
# OPERATION 2: SEARCH for a supplier by name
# ─────────────────────────────────────────
def search_supplier(name):
    # If name is not a key in the dictionary, stop here
    if name not in roster:
        print(f"  [!] Supplier '{name}' not found.")
        return

    # Retrieve and display the supplier's details
    info = roster[name]
    print(f"\n  Name      : {name}")
    print(f"  Email     : {info['email']}")
    print(f"  Join date : {info['join_date']}")


# ─────────────────────────────────────────
# OPERATION 3: DELETE a supplier by name
# ─────────────────────────────────────────
def delete_supplier(name):
    # Cannot delete someone who does not exist
    if name not in roster:
        print(f"  [!] Supplier '{name}' not found. Nothing was deleted.")
        return

    # Remove the key-value pair from the dictionary
    del roster[name]
    print(f"  [OK] Supplier '{name}' has been deleted.")


# ─────────────────────────────────────────
# OPERATION 4: LIST all suppliers in the roster
# ─────────────────────────────────────────
def list_all():
    # Handle the case where no suppliers have been added yet
    if not roster:
        print("  (The roster is currently empty.)")
        return

    # Print a formatted table header
    print(f"\n  {'Name':<20} {'Email':<30} {'Join Date'}")
    print(f"  {'-' * 20} {'-' * 30} {'-' * 10}")

    # Loop through every supplier and print their info
    for name, info in roster.items():
        print(f"  {name:<20} {info['email']:<30} {info['join_date']}")


# ─────────────────────────────────────────
# INPUT HELPER 1: Ask user for a non-empty text field
# Keeps asking until the user types something real
# ─────────────────────────────────────────
def prompt(label):
    while True:
        value = input(f"  {label}: ").strip()  # .strip() removes accidental spaces
        if value:
            return value  # Only return when the input is not empty
        print("  [!] This field cannot be empty. Please try again.")


# ─────────────────────────────────────────
# INPUT HELPER 2: Ask user for a valid date
# Must be in YYYY-MM-DD format, e.g. 2024-03-25
# ─────────────────────────────────────────
def prompt_date():
    while True:
        raw = input("  Join date (YYYY-MM-DD): ").strip()
        try:
            # date.fromisoformat() will raise ValueError if format is wrong
            date.fromisoformat(raw)
            return raw  # Format is valid, return the date string
        except ValueError:
            print("  [!] Invalid date format. Please use YYYY-MM-DD (e.g. 2024-03-25).")

# ─────────────────────────────────────────
# INPUT HELPER 3: Ask user for a valid email address
# Checks format using a regular expression (regex)
# Valid example:  supplier@company.com
# Invalid example: supplier@com  /  supplier  /  @company.com
# ─────────────────────────────────────────
def prompt_email():
    # Regex pattern that covers standard email formats
    # Breakdown:
    #   [^@\s]+   = one or more characters that are NOT @ or space (the username)
    #   @         = the @ symbol
    #   [^@\s]+   = one or more characters (the domain name, e.g. gmail)
    #   \.        = a literal dot
    #   [^@\s]+   = one or more characters (the extension, e.g. com)
    email_pattern = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

    while True:
        value = input("  Email address: ").strip()

        if not value:
            print("  [!] Email cannot be empty. Please try again.")
            continue

        if not email_pattern.match(value):
            print("  [!] Invalid email format. Please enter a valid email (e.g. name@company.com).")
            continue

        # Email passed both checks — return it
        return value



# ─────────────────────────────────────────
# MENU: Display the options to the user
# ─────────────────────────────────────────
def show_menu():
    print("\n" + "=" * 42)
    print("    Supplier Roster Manager")
    print("=" * 42)
    print("  1. Add a supplier")
    print("  2. Search for a supplier")
    print("  3. Delete a supplier")
    print("  4. List all suppliers")
    print("  0. Exit")
    print("=" * 42)


# ─────────────────────────────────────────
# MAIN FUNCTION: Program entry point
# Runs the menu loop until the user exits
# ─────────────────────────────────────────
def main():
    print("Welcome to the Supplier Roster Manager!")

    while True:
        show_menu()

        try:
            # Read the user's menu choice
            choice = input("  Enter your choice (0-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or unexpected input gracefully
            print("\n\n  Goodbye!")
            break

        if choice == "1":
            print("\n  -- Add Supplier --")
            name      = prompt("Supplier name")
            email = prompt_email()
            join_date = prompt_date()
            add_supplier(name, email, join_date)

        elif choice == "2":
            print("\n  -- Search Supplier --")
            name = prompt("Enter supplier name to search")
            search_supplier(name)

        elif choice == "3":
            print("\n  -- Delete Supplier --")
            name = prompt("Enter supplier name to delete")
            delete_supplier(name)

        elif choice == "4":
            print("\n  -- All Suppliers --")
            list_all()

        elif choice == "0":
            # User chose to exit cleanly
            print("\n  Goodbye!")
            break

        else:
            # Catch any input that is not 0-4
            print("  [!] Invalid choice. Please enter a number between 0 and 4.")


# ─────────────────────────────────────────
# Run the program only when executed directly
# (not when imported as a module)
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()