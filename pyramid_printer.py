def print_char_pyramid(char, levels):
    for i in range(levels):
        # Calculate the number of spaces on each side
        spaces = ' ' * (levels - i - 1)

        # Calculate the repetition of the character
        char_repetition = char * (2 * i + 1)

        # Construct and print the line
        print(spaces + char_repetition + spaces)

# Example usage: Print 50 levels of "AAAAAAAA" :)
print_char_pyramid("A", 50)