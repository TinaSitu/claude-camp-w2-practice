"""
Exercise 4: Safe Calculator (安全的计算器)
A command-line calculator that supports addition, subtraction,
multiplication and division. Handles all invalid inputs gracefully
without crashing — including division by zero and non-numeric input.

Key concepts:
- Float input validation with try/except
- Division by zero handling
- While loop for continuous operation
- Clean exit with quit command
"""


# ─────────────────────────────────────────
# INPUT HELPER: Ask user for a number
# Keeps asking until a valid number is entered
# or the user types quit to exit the program
# ─────────────────────────────────────────
def get_number(prompt):
    while True:
        value = input(f"  {prompt}: ").strip()

        # Allow user to quit at any input step
        if value.lower() == "quit":
            print("\n  Goodbye!")
            exit()

        try:
            # Try converting the input to a float
            # This handles integers, decimals, and negatives
            return float(value)
        except ValueError:
            # Input was not a number — warn and ask again
            print(f"  [!] '{value}' is not a valid number. Please try again.")


# ─────────────────────────────────────────
# INPUT HELPER: Ask user for an operator
# Only accepts +, -, *, /
# ─────────────────────────────────────────
def get_operator():
    valid_operators = ["+", "-", "*", "/"]

    while True:
        operator = input("  Operator (+, -, *, /): ").strip()

        # Allow user to quit at any input step
        if operator.lower() == "quit":
            print("\n  Goodbye!")
            exit()

        if operator in valid_operators:
            return operator

        # Operator was not one of the four valid options
        print(f"  [!] '{operator}' is not a valid operator. Please use +, -, *, or /")


# ─────────────────────────────────────────
# CORE FUNCTION: Perform the calculation
# Returns the result or None if division by zero
# ─────────────────────────────────────────
def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":
        # Division by zero is mathematically undefined — handle gracefully
        if number2 == 0:
            print("  [!] Error: cannot divide by zero.")
            return None

        return number1 / number2


# ─────────────────────────────────────────
# DISPLAY HELPER: Format the result nicely
# Shows integers without decimal point (e.g. 6 not 6.0)
# Shows decimals up to 6 places (e.g. 3.141593)
# ─────────────────────────────────────────
def format_number(value):
    # If the number is a whole number, show it as an integer
    if value == int(value):
        return str(int(value))

    # Otherwise show up to 6 decimal places, stripping trailing zeros
    return f"{value:.6f}".rstrip("0")


# ─────────────────────────────────────────
# MAIN FUNCTION: Program entry point
# Runs the calculator in a loop until user quits
# ─────────────────────────────────────────
def main():
    print("Welcome to the Safe Calculator!")
    print("  Tip: type 'quit' at any time to exit.\n")

    while True:
        print("─" * 42)

        # Step 1: Get first number
        number1 = get_number("First number")

        # Step 2: Get operator
        operator = get_operator()

        # Step 3: Get second number
        number2 = get_number("Second number")

        # Step 4: Perform calculation
        result = calculate(number1, operator, number2)

        # Step 5: Display result if calculation was successful
        if result is not None:
            # Format each number cleanly for display
            n1 = format_number(number1)
            n2 = format_number(number2)
            r  = format_number(result)
            print(f"\n  {n1} {operator} {n2} = {r}\n")

        # Step 6: Ask if user wants to calculate again
        again = input("  Calculate again? (yes / quit): ").strip().lower()
        if again in ["quit", "q", "no", "n"]:
            print("\n  Goodbye!")
            break


# ─────────────────────────────────────────
# Run only when executed directly
# (not when imported as a module)
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()