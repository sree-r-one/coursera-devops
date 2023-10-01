"""
This is a sample module to demonstrate docstrings
"""


def add(number1, number2):
    """
    Adding this and that

    """

    return number1 + number2


NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
# print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))
print(f"This is a test {NUM1}")
