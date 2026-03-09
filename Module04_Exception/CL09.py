### This template is for the class demo and exercises covered in M03_Lec09_exception for CS 22B.

# print(x)  # This will raise a NameError since x is not defined.

try :
    print(x)
except NameError:
	print("NameError; undefined variable or function")
 
y=10
try:
    if not type(y) is str:
        raise TypeError("y should be a string")
except NameError:
	print("NameError; undefined variable or function")
except ZeroDivisionError:
    print("Cannot divide by Zero")
except Exception as error:
    print(error)
    
else:
    print("No errors. Yay!")
finally:
    print("This will print in all cases")
    
    
### Example error in function, then try-except block to handle it.
def divide_with_even(y,x):
    if x%2 != 0:
        raise Exception("Sorry, no non-even numbers")
    return y/x

try:
    print(divide_with_even(10,3)) #try with (20,4)
except Exception as error:
    print(error)
    
### Exception object
number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

number2 = 20
assert (number2 < 5), f"The number should not exceed 10. ({number2=})"
print(number2)
