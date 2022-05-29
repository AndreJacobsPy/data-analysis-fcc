import numpy as np


def calculate(numbers: list):
    """This function gives summary statistics for an eight item list. The list is converted
    into a 3 by numpy array are gives stats for the rows, columns and for the flattened array.

    Arguments:
        numbers: this is a list containing integers or floats. must be 9 items long.

    Returns:
        stats: a dictionary providing different statistics based on different parts of
        the numpy array that is made form the list.
    """

    if len(numbers) != 9:
        return ValueError('ValueError: Not the correct length of list')

    df = np.array(numbers).reshape(3, 3)
    summary = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    return df, summary


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

