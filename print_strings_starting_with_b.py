def print_strings_starting_with_b(strings: list[str]) -> None:
    """
    Prints all strings from the input list that start with the letter 'B' or 'b'.
    
    This function iterates through a list of strings, checking if each string 
    begins with the letter 'B' or 'b' (case-insensitive). If a string starts 
    with either of these letters, it is printed to the console.

    Parameters:
    strings (list): A list of strings to be checked.
    """
    for string in strings:
        if len(string) > 0 and string[0].lower() == 'b':  # Check first character
            print(string)

if __name__ == "__main__":
    # Example usage
    strings = ['Bosch', 'Bangalore', 'Mexico', 'Canada', 'India']
    print_strings_starting_with_b(strings)