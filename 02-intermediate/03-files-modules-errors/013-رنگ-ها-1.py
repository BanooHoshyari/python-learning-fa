# --- Simple Code 2.b: Colors from user (More Professional Approach) ---

# 1. Ask the user to enter all colors on one line, separated by spaces.
# Example input: red blue green yellow
input_string = input("Please enter colors separated by spaces (e.g., red blue green): ")

# 2. Convert the input string into a list of colors using the split() method.
# split() by default splits the string based on whitespace (spaces, tabs, newlines).
# If the input is "red blue green", colors_list will become: ['red', 'blue', 'green']
colors_list = input_string.split()

# 3. Convert the resulting list into a tuple.
colors = tuple(colors_list)

# 4. Print the final tuple.
print("Tuple of colors:", colors)

# Example of running this code:
# Please enter colors separated by spaces (e.g., red blue green): purple orange pink
# Tuple of colors: ('purple', 'orange', 'pink')
