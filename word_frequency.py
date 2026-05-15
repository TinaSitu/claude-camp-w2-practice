"""
Exercise 2: Word Frequency Counter
Takes a block of text input from the user and counts how many
times each word appears, sorted from highest to lowest frequency.

Key concepts:
- Dictionary for storing word counts
- String methods for cleaning and splitting text
- Sorting with key functions
- Multi-line input handling
"""

import re


# ─────────────────────────────────────────
# CORE FUNCTION: Count word frequencies
# Takes a string of text and returns a dictionary
# where key = word, value = number of times it appears
# Example: {"hello": 3, "world": 1}
# ─────────────────────────────────────────
def count_words(text):
    # Convert all text to lowercase so "Hello" and "hello" count as the same word
    text = text.lower()

    # Use regex to extract only real words (letters only)
    # This automatically removes punctuation like commas, periods, exclamation marks
    words = re.findall(r'\b[a-z]+\b', text)

    # If no words were found after cleaning, return empty dictionary
    if not words:
        return {}

    # Count each word using a dictionary
    frequency = {}
    for word in words:
        if word in frequency:
            # Word already seen — increment its count by 1
            frequency[word] += 1
        else:
            # First time seeing this word — start count at 1
            frequency[word] = 1

    return frequency


# ─────────────────────────────────────────
# DISPLAY FUNCTION: Print results as a sorted table
# Sorted from highest frequency to lowest
# ─────────────────────────────────────────
def display_results(frequency):
    if not frequency:
        print("\n  [!] No words found. Please enter some text.")
        return

    # Sort the dictionary by value (count) in descending order
    # sorted() returns a list of (word, count) tuples
    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    # Calculate totals for the summary line
    total_words = sum(frequency.values())
    unique_words = len(frequency)

    # Get the highest count for scaling the visual bar
    max_count = sorted_words[0][1]

    # Print table header
    print(f"\n  {'─' * 40}")
    print(f"  {'Word':<20} {'Count':>6}   Bar")
    print(f"  {'─' * 40}")

    # Print each word with its count and a visual bar made of # symbols
    for word, count in sorted_words:
        bar_length = int((count / max_count) * 20)
        bar = "#" * bar_length
        print(f"  {word:<20} {count:>6}   {bar}")

    # Print summary footer
    print(f"  {'─' * 40}")
    print(f"  Total words  : {total_words}")
    print(f"  Unique words : {unique_words}")
    print(f"  {'─' * 40}")


# ─────────────────────────────────────────
# INPUT FUNCTION: Collect multi-line text from user
# User types their text across multiple lines
# then types END on a new line to finish
# ─────────────────────────────────────────
def get_text_input():
    print("\n  Enter your text below.")
    print("  When finished, type END on a new line and press Enter.")
    print("  " + "─" * 40)

    lines = []
    while True:
        try:
            line = input("  ")
            # Stop collecting when user types END
            if line.strip().upper() == "END":
                break
            lines.append(line)
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input cancelled.")
            break

    # Join all lines into one single block of text
    return " ".join(lines)


# ─────────────────────────────────────────
# SAMPLE TEXT: Built-in demo text for quick testing
# ─────────────────────────────────────────
SAMPLE_TEXT = """
Python is a great programming language. Python is easy to learn and easy to use.
Many developers love Python because Python is powerful and Python is fun.
Learning Python every day makes you a better developer every day.
"""


# ─────────────────────────────────────────
# MENU: Display the options to the user
# ─────────────────────────────────────────
def show_menu():
    print("\n" + "=" * 42)
    print("    Word Frequency Counter")
    print("=" * 42)
    print("  1. Analyse my own text")
    print("  2. Analyse sample text (quick test)")
    print("  0. Exit")
    print("=" * 42)


# ─────────────────────────────────────────
# MAIN FUNCTION: Program entry point
# Runs the menu loop until the user exits
# ─────────────────────────────────────────
def main():
    print("Welcome to the Word Frequency Counter!")

    while True:
        show_menu()

        try:
            choice = input("  Enter your choice (0-2): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  Goodbye!")
            break

        if choice == "1":
            # Get text typed by the user
            text = get_text_input()

            if not text.strip():
                print("\n  [!] No text entered. Please try again.")
                continue

            # Count words and show results
            frequency = count_words(text)
            display_results(frequency)

        elif choice == "2":
            # Run the built-in sample text for quick testing
            print("\n  Sample text:")
            print(f"  {SAMPLE_TEXT.strip()}")
            frequency = count_words(SAMPLE_TEXT)
            display_results(frequency)

        elif choice == "0":
            print("\n  Goodbye!")
            break

        else:
            print("  [!] Invalid choice. Please enter 0, 1, or 2.")


# ─────────────────────────────────────────
# Run only when executed directly
# (not when imported as a module)
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()