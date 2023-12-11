
# Author: Shivanesh Lal
# Date: 11/12/2023
# Version: 1.0.0

__version__ = '1.0.0'
__author__ = 'Shivanesh Lal'

# Python program to print numbers from 1 to 100
# For multiples of 3, it prints "Bula"
# For multiples of 5, it prints "Vinaka"
# For multiples of both 3 and 5, it prints "BulaVinaka"

# Function to create a table with version, author, and output
def create_table_with_output(version, author):
    # Define the top part of the table
    table_top = '+' + '-'*18 + '+' + '-'*20 + '+'
    # Define the header part of the table
    header = '| {:<11} | {:<20} |'.format('Output', 'Type')
    # Initialize the table with the top and the header
    table = [table_top, header, table_top]

    # Iterate through the numbers and add each to the table with its corresponding output
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            output = "BulaVinaka"
            type_descr = "Multiple of 3 and 5"
        elif number % 3 == 0:
            output = "Bula"
            type_descr = "Multiple of 3"
        elif number % 5 == 0:
            output = "Vinaka"
            type_descr = "Multiple of 5"
        else:
            output = str(number)
            type_descr = "Other"

        # Add the row for this number to the table
        table.append('| {:<11} | {:<20} |'.format(output, type_descr))

    # Add the final part of the table with version and author information
    table.append(table_top)
    table.append('| {:<11} | {:<20} |'.format('Version', version))
    table.append('| {:<11} | {:<20} |'.format('Author', author))
    table.append(table_top)

    # Join all the parts of the table and return
    return '\n'.join(table)

# Print the table
print(create_table_with_output(__version__, __author__))

# Here's the thought process and explanation of the solution:
# This program utilizes basic control flow with if-elif-else statements to determine
# what to print for each number in the range.
# The modulus operator is the key to determining multiples,
# as it returns the remainder after division—if the remainder is 0,
# the number is a multiple of the divisor.
