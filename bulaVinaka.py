# Author: Shivanesh Lal
# Date: 11/12/2023
# Version: 1.0.0

__version__ = '1.0.0'
__author__ = 'Shivanesh Lal'

# Python program to print numbers from 1 to 100
# For multiples of 3, it prints "Bula"
# For multiples of 5, it prints "Vinaka"
# For multiples of both 3 and 5, it prints "BulaVinaka"

# Function to create the table
def create_table_with_output_and_summary(version, author):
    # Initialize counters for each type
    count_multiple_3 = 0
    count_multiple_5 = 0
    count_multiple_3_and_5 = 0
    count_other = 0

    # Define the top part of the table
    table_top = '+' + '-'*20 + '+' + '-'*25 + '+'
    # Define the header part of the table
    header = '| {:<20} | {:<20} |'.format('Output', 'Type')
    # Initialize the table with the top and the header
    table = [table_top, header, table_top]

    # Iterate through the numbers and add each to the table with its corresponding output
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            output = "BulaVinaka"
            type_descr = "Multiple of 3 and 5"
            count_multiple_3_and_5 += 1
        elif number % 3 == 0:
            output = "Bula"
            type_descr = "Multiple of 3"
            count_multiple_3 += 1
        elif number % 5 == 0:
            output = "Vinaka"
            type_descr = "Multiple of 5"
            count_multiple_5 += 1
        else:
            output = str(number)
            type_descr = "Other"
            count_other += 1

        # Add the row for this number to the table
        table.append('| {:<20} | {:<20} |'.format(output, type_descr))

    # Add a summary row
    table.append(table_top)
    table.append('| {:<20} | {:<20} |'.format('Total Multiples of 3', str(count_multiple_3)))
    table.append('| {:<20} | {:<20} |'.format('Total Multiples of 5', str(count_multiple_5)))
    table.append('| {:<20} | {:<20} |'.format('Total of Both 3 & 5', str(count_multiple_3_and_5)))
    table.append('| {:<20} | {:<20} |'.format('Total Others', str(count_other)))

    # Add the final part of the table with version and author information
    table.append(table_top)
    table.append('| {:<20} | {:<20} |'.format('Version', version))
    table.append('| {:<20} | {:<20} |'.format('Author', author))
    table.append(table_top)

    # Join all the parts of the table and return
    return '\n'.join(table)

# Print the table
print(create_table_with_output_and_summary(__version__, __author__))

# Here's the thought process and explanation of the solution:
# This program utilizes basic control flow with if-elif-else statements to determine
# what to print for each number in the range.
# The modulus operator is the key to determining multiples,
# as it returns the remainder after division—if the remainder is 0,
# the number is a multiple of the divisor.
