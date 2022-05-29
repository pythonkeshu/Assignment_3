#Q1.  Write a Python function to sum all the numbers in a list.

    
def sum_of_list():
    given_list = map(int, input("Enter the list followed by space: ").split(" "))
    
    total = sum(given_list)
    print("final result :",total)
    return total
sum_of_list()
      



    
        