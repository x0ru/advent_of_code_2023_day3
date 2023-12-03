import csv

"""
List of indexes where signs and numbers occur
"""

signs_index_list = []
numbers_index_list = []
cog_index_list = []

"""
Helps creating a matrix format [line_indicator x index]
"""

line_indicator = 1

"""
Number and signs (not including .  <-- dot).
"""

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = ['!', '@', '#', "$", '%', '^', '&', '*', '(', ')', '-', '+', '=', '/']
res = 0
cog = '*'

with open("file.csv") as file:
    file = csv.reader(file)
    for line in file:

        """
        Opening the file and splitting each line to become list of each char.
        """

        split = [*(line[0])]

        """
        Index list of number occurrence.
        """

        index_list = []

        """
        Will help create full number and turn it to the int.
        """

        number = ''

        """
        First for loop checks if char is in signs list if yes it add it to our list all
        occurrences of special signs. Format: [1st argument nr of line, 2nd argument index in this line].
        """

        for index, letter in enumerate(split):
            if letter in signs:
                signs_index_list.append([line_indicator, index])

        """
        Second for loop checks if char is in numbers.
        """

        for index, letter in enumerate(split):

            """
            First part just check for individual char because it is string. Then concat it to var number.
            Second part append to the index_list  occurrence of number.
            Format: [1st argument nr of line, 2nd argument index in this line]. 
            """

            if letter in numbers:
                number += letter
                index_list.append([line_indicator, index])

            """
            This if checks if var number is not an empty string (it would mean previous char/chars were in numbers)
            and are stored in var number. If next char is not number or it is end of the line, join the char in str
            (so far they were just separated chars in list). Next Step we reset number var for next number.
            Finally append it in format [1st argument: int full number, 
            2nd argument: list withing list of all occurrences of number 
            [1st argument nr of line, 2nd argument index in this line]].
            """

            if (letter not in numbers and number != '') or (number != '' and index == len(split) - 1):
                number_to_calc = ''.join(number)
                number = ''
                numbers_index_list.append([int(number_to_calc), index_list])
                index_list = []

        for index, letter in enumerate(split):
            if letter in cog:
                cog_index_list.append([line_indicator, index])

        """
        Here where we add to line indicator when we read entire line.
        """

        line_indicator += 1

        """
        Last loop where we compare if each full number is attached to any sign.
        In element[1] we have list of lists example : [[],[],[]] and each list inside has to be compared
        with sings_index_lists. If they match we add number element[0] to res and break the loop.
        (The reason we use break is simple fact that each number might be attached to more than on sign.
        We want to check if it is attached to any so one time we add it to result.
        """

    for element in numbers_index_list:
        for indexes in element[1]:

            """
            Check right, left , down,  down-left, down-right, up, up-left, up-right.
            """

            if [int(indexes[0]), int(indexes[1] + 1)] in signs_index_list or \
                [int(indexes[0]), int(indexes[1] - 1)] in signs_index_list or \
                [int(indexes[0]) - 1, int(indexes[1])] in signs_index_list or \
                [int(indexes[0]) - 1, int(indexes[1] - 1)] in signs_index_list or \
                [int(indexes[0]) - 1, int(indexes[1] + 1)] in signs_index_list or \
                [int(indexes[0]) + 1, int(indexes[1])] in signs_index_list or \
                [int(indexes[0]) + 1, int(indexes[1] - 1)] in signs_index_list or \
                    [int(indexes[0]) + 1, int(indexes[1]) + 1] in signs_index_list:
                res += element[0]
                break

print(res)

"""
Second star.  hold_first_number - holds first number to multiply.
"""

res2 = 0
hold_first_number = 0


"""
Same approach as in part 1 only now we check list of cogs in list of indexes of numbers.
"""

for cog in cog_index_list:

    """
    Set hold_first_number to zero when we checking next cog. Three possible outcomes.
    1. Cog is not attached to any number. hold_first_number was 0 in that case .
    2. Cog is attached to one number. We are moving to next cog. hold_first_number has to be set back to 0.
    3. Cog is attached to two numbers. If statement hold_first_number > 0. 
    """

    hold_first_number = 0
    for index in numbers_index_list:

        """
        Check right, left , down,  down-left, down-right, up, up-left, up-right.
        """

        if [int(cog[0]), int(cog[1] + 1)] in index[1] or \
                [int(cog[0]), int(cog[1] - 1)] in index[1] or \
                [int(cog[0]) - 1, int(cog[1])] in index[1] or \
                [int(cog[0]) - 1, int(cog[1] - 1)] in index[1] or \
                [int(cog[0]) - 1, int(cog[1] + 1)] in index[1] or \
                [int(cog[0]) + 1, int(cog[1])] in index[1] or \
                [int(cog[0]) + 1, int(cog[1] - 1)] in index[1] or \
                [int(cog[0]) + 1, int(cog[1]) + 1] in index[1]:
            if hold_first_number > 0:

                """
                Cog is attached to number we multiply first number which we stored in hold_first_number by index[0]
                which is second number attached to cog.
                hold_first_number set to 0 because there might be more cogs on the same line of text.
                """

                res2 += hold_first_number * index[0]
                hold_first_number = 0

            """
            Add current number attached to cog to var.
            """

            hold_first_number += index[0]


print(res2)
