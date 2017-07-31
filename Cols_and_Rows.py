from itertools import count, product, islice
import pandas as pd
import numpy as np
import random
import string


# Prompts the user to enter the desired number of columns and rows, returns both.
def UserPrompt():
    print("Hello, User.")
    user_rows = int(input(print("\nPlease enter the number of rows in your dataset")))
    user_columns = int(input(print("\nPlease enter the number of columns in your dataset")))
    return user_rows, user_columns

# Generates a list of header titles based on the entered number of columns, in the form of A-Z, AA-ZZ, AAA-ZZZ etc
def ColumnGenerator():
    columns_headers = string.ascii_uppercase
    for each in count(1):
        for all in product(columns_headers, repeat=each):
           yield ''.join(all)

# Generates a matrix with the user defined row/col sizes, generates random int values to populate the matrix
# Returns a list of lists, ex ([1,2,3],[4,5,6],[7,8,9]) for a 3x3 matrix
def RowGenerator(number_of_rows, row_length):
    rows_list = []
    for number in range(number_of_rows):
        group_list = []
        for value in range(row_length):
            value = random.randrange(1, 10000)
            group_list.append(value)
        rows_list.append(group_list)
    return rows_list

# Generates the Dataframe using Pandas, applies header titles, print the matrix, and computes
# the standard deviation for each column group
def DataFrameGenerator(Data, Headers):
    df = pd.DataFrame(np.array(data_set), columns=headers)
    print(df)
    print(np.std(df))


if __name__ == '__main__':
    size = UserPrompt()
    rows = size[0]
    cols = size[1]
    print("Rows = " + str(rows))
    print("Columns = " + str(cols))
    data_set = RowGenerator(rows, cols)
    headers = list(islice(ColumnGenerator(), cols))
    DataFrameGenerator(data_set, headers)
