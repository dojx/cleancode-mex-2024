# Receives an array of strings and prints all strings starting with "B" or "b"
def print_strings_starting_with_b(strings):
    for string in strings:
        if len(string) > 0 and string[0].lower() == 'b':  # Check first character
            print(string)

if __name__ == "__main__":
    # Example usage
    strings = ['Bosch', 'Bangalore', 'Mexico', 'Canada', 'India']
    print_strings_starting_with_b(strings)