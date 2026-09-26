"""

for loop: sequence of statements is executed multiple 
          times and abbreviates the code that manages the loop variable.

          syntax:

          for variable in sequence:
              statement(s)

"""

for i in range(1, 6):
    print(i)

    """
    range([start], stop[, step]):
     
     returns a sequence of numbers, 
     starting from 0 by default, 
     and increments by 1 (by default), and stops before a specified number.

     range(4) is equivalent to range(0, 4) and returns 0, 1, 2, 3.
     range(1, 4) returns 1, 2, 3.
     step : by default by +1     
    """
    for i in range(1, 10, 2):
        print(i)


        