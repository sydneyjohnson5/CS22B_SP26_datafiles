### This template is for the class demo and exercises covered in M03_Lec07_function for CS 22B.

### Example of function with docstring
## to print docstring call <fxn>.__docstring__
def get_at_content(dna:str) -> float:
    '''Function computes the proportion of A's and T's in dna. 
Args:
         dna: string param
    Returns:
       	at_content: type(float) between 0 and 1, inclusively
    '''
    length = len(dna)
    a_count = dna.count('A')  
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

##### CL7.2 Comparing functions
lsti = [1, 2, 3]
def my_function1(i):
	i.extend(['a', 'b', 'c'])
	return(i) 
lst = my_function1(lsti)

def my_function2(i):
	return(i + ['a', 'b', 'c'])
lst2 = my_function2(lsti)


##### CL7.3 Write a functional program
## Why is this code not functional?
total = 0
for i in range(1, 11):
    total += i*i
print("First run, total = "+ str(total))

for i in range(1, 11):
    total += i*i
print("Second run, total = "+ str(total))

## Rewrite this code so it is functional
## Functional because no mutable variable, uses generator expression


##### CL7.4: Example of using map() 
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4]
print("Before running map func, numbers is")
print(numbers)
squared_numbers = list(map(square, numbers))
print("squared_numbers = " + str(squared_numbers))
print("numbers = " + str(numbers))


##### CL7.5 map() with lambda function
stringlist = ["and", "ant", "air", "anything"]
bstring = list(map(lambda x:x.replace("a", "B"),stringlist))
print(bstring)


##### CL7.6 filter() function
num_input= [1, 4, 5, 20, 15, 70, 15, 6, 7, 70]

def greater100(num):
    return num ** 2 >= 100

### Using filter with a lambda function that calls greater100


##### CL7.7 Higher order sorted
## Sort this list of tuples by second element in reverse order
vegfruit = [(1, "zuchinni"), (3, "carrot"), (2, "apple"), (5, "orange"), (4, "banana")]

#sortedname = sorted()
#print(sortedname)


##### CL7.8 Writing functional code with higher order
## Rewrite this procedurally written code into functional style using map(), lambda, sum()
total2 = 0
for i in range(1, 21):
    if i % 2 == 0:
        total2 += i**2
    else:
        total2 += i**3

## Functional because no state change, no explicit loop, and is pure
total2 = sum(map(lambda i: i**2 if i % 2 == 0 else i**3, range(1, 21)))
#print(total2)