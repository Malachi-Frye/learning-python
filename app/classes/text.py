# when given a string, return the length of the string

# when given a STRING
def stringlength(string):
# COUNT the CHAR in the STRING
    counter = 0 
    for char in string: 
        counter = counter + 1 
         
# return COUNT
    return counter 
# when given a string and a number in the string, return the charcter 
result = stringlength("Debug me")
print(result)
