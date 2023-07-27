#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [] 
    for row in matrix:
      new_row = [] 
      for number in row:
         new_number = number ** 2
         new_row.append(new_number) #new results
      new_matrix.append(new_row)
    return new_matrix

def display_new_matrix(matrix=[]):
    for row in matrix:
      print(", ".join(str(number)for number in row))
