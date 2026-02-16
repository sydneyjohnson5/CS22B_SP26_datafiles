### CS 22B Module 01 - Homework 1
### Name: Sydney Johnson

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters. 
## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file,  bad_reads.txt. 
## 4. Print as output, the number of valid and invalid reads. 

root = r"C:\Users\sydne\OneDrive\Documents\CS_22B\CS22B_SP26_datafiles\CS22B_SP26_datafiles\Module01_Essentials\\"

valid_reads = []
invalid_reads = [] 

with open(root + "adapter_reads.txt", "r") as infile, \
     open(root + "clean_reads.txt", "w") as clean, \
     open(root + "bad_reads.txt", "w") as bad:


    for line in infile:
        read = line.strip()

        # Trim first 14 bases
        trimmed = read[14:]

        # Validate characters
        if all(base in {"A", "T", "C", "G"} for base in trimmed):
            valid_reads.append(trimmed)
            clean.write(trimmed + "\n")
        else:
            invalid_reads.append(trimmed)
            bad.write(trimmed + "\n")

print("Valid reads:", len(valid_reads))
print("Invalid reads:", len(invalid_reads))



##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read. 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length). 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

# List of Lengths
lengths = [len(r) for r in valid_reads]

# List of GC Percentages
gc_percents = [(r.count("G") + r.count("C")) / len(r) for r in valid_reads]

# Print Statistics
min_len = min(lengths)
max_len = max(lengths)
avg_len = sum(lengths) / len(lengths)
avg_gc = sum(gc_percents) / len(gc_percents)

print("Min lengths:", min_len)
print("Max length:", max_len)
print("Average length:", round(avg_len, 3))
print("Average GC Precent:", round(avg_gc, 3))

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads. 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).
base_counts = {"A": 0, "T": 0, "C": 0, "G": 0}

for read in valid_reads:
    for base in read:
        base_counts[base] += 1

print("Base counts:", base_counts)

#Prodcut of A*C*T*G
product = 1
for base in base_counts:
    product *= base_counts[base]

print("Product A*C*T*G =", product)

#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.

## Use this sequence as your test sequence
sequence = "TTATAAGCCGATTATAAGCCCGTAACCGGTTAG"

def nt_percent(seq, nt):
    percent = (seq.count(nt) / len(seq)) *100
    return round(percent, 2)

assert nt_percent("AATT", "A") == 50.00
assert nt_percent("CCCC", "A") == 0.00
assert nt_percent("ATGC", "T") == 25.00

print("Percent A:", nt_percent(sequence, "A"))
print("Percent T:", nt_percent(sequence, "T"))
print("Percent C:", nt_percent(sequence, "C"))
print("Percent G:", nt_percent(sequence, "G"))
      
