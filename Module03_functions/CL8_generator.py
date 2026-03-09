### This template is for the class demo and exercises covered in M03_Lec08_generator for CS 22B.

### Example of generator expression vs normal function
xs = [1, 2, 3, 4, 5]
xs_squared_list = [xs_item * xs_item for xs_item in xs]
print("xs_squared_list: ", xs_squared_list)

##xs_squared_gen = (xs_item * xs_item for xs_item in xs) --- IGNORE ---
xs_squared_gen = (xs_item * xs_item for xs_item in xs)
print("xs_squared_gen object: ", xs_squared_gen) #returns a generator object, not the list of squared values

## How to get the values from generator object? 


##### CL8.1 Comparing functions
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1
        print(i, "hello")

genobj1 = count_up_to(5)
for x in genobj1:
    print(x)
    
genobj2 = count_up_to(5)
print("print(next(genobj2)):", next(genobj2))


##### CL8.2 Re-writing function as a generator expression
## Procedural code modify state of total at each iteration, that is 'total' is a mutable variable. 
## This code is not functional.
total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i**2
    else:
        total += i**3

print("total:", total)

## Rewrite this procedurally written code using a generator expression with no intermediate lists
## Goal is no state change, no explicit loop, and is pure
# total_gen = 
