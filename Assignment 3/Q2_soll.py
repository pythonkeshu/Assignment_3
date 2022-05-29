#Q2.Write a Python program to reverse a string.
def reverse(given_data):
  str = ""
  for i in given_data:
    str = i + str
  return str
  
given_data = (input("enter the data you want to reverse : "))
  
print ("The original string  is : ",end="")
print (given_data)
  
print ("The reversed string is : ",end="")
print(reverse(given_data))