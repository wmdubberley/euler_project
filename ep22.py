def calculate_alphabetical_value(name):
    # Calculate the alphabetical value of the name
    return sum(ord(char) - ord('A') + 1 for char in name)

def calculate_total_name_scores(filename):
    # Read the file
    with open(filename, 'r') as file:
        data = file.read()
    
    # Strip the quotes and split the names into a list
    names = data.replace('"', '').split(',')
    
    # Sort the list of names alphabetically
    names.sort()
    
    total_score = 0
    
    # Calculate the total score
    for i, name in enumerate(names):
        alphabetical_value = calculate_alphabetical_value(name)
        name_score = alphabetical_value * (i + 1)  # Multiply by the 1-based index (position in sorted list)
        total_score += name_score
    
    return total_score

# Example usage
filename = './0022_names.txt'  # Replace this with the path to your 'names.txt' file
total_name_scores = calculate_total_name_scores(filename)
print(f"The total of all the name scores in the file is: {total_name_scores}")
