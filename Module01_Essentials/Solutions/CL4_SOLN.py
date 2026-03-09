### This template is for the class exercises covered in M01_L03_review-fxn-condition for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL4.1: Writing a function 
### Write a function that takes two arguments; a DNA sequence and a nucleotide (ie., “A”, “T”, “C” or “G”). Return the percentage of the DNA sequence that the nucleotide makes up.

dna = "ATTGGCTATACCGGCATCGGGTAGCC"

# step 1: Write the function that takes in two argument and calculate (num of nucleotide)*100/(total nucleotide)

def get_percent(sequence, nt):
    count_nt = sequence.count(nt)
    percent = count_nt*100/len(sequence)
    return percent

percent = get_percent(dna, "A")
print("Percent: " + str(percent) + "%.")

# step 2: modify the function above to pass in a third argument to return 2 significant figures

def get_percent_2sig(sequence, nt, sig_fig=2):
    count_nt = sequence.count(nt)
    percent = count_nt*100/len(sequence)
    return round(percent, 2)

percent = get_percent_2sig(dna, "A")
print("Percent: " + str(percent) + "%.")

##### CL4.2: Using assert to test your function
### Write assertion statements to test your function, get_percent_2sig.
### Part A.: Write assertion that takes in sequence and nucleotide [“A”]
test_dna = "AATT"
assert get_percent_2sig(test_dna, "A") == 50

### Part B.: If you change the assertion so that the  expected result is 0.80, what is your output?

# returns Assertion Error, so comment out so code won't fail
#assert get_percent_2sig(test_dna, "A") == 0.80

##### CL4.3: Conditional statements
### Find the accession that starts with ‘a’

accession_name = ['ab56', 'bh84', 'hg84', 'ay97', 'cd72', 'ef56']

### step 1: Write a for loop that iterates over the accession_name list 

#for acc in accession_name:

### step 2: Use a conditional statement to ask if the accession name starts with ‘a’ and if it does, print out the name
for acc in accession_name:
    if acc.startswith('a'):
        print(acc)

##### CL4.4: if-elif-else 
### Write three files of accession names; one start with ‘a’, one start with ‘b’, and last one has all others accession names.

accession_name = ['ab56', 'bh84', 'hg84', 'ay97', 'cd72', 'ef56']

### step 1: Write three files
afile = open("a_accession.txt", "w")
bfile = open("b_accession.txt", "w")
otherfile = open("not_ab_accession.txt", "w")

### step 2: Iterate over the list of accession names and sort them into the correct files.
for name in accession_name:
    if name.startswith("a"):
        afile.write(name + "\n")
    elif name.startswith("b"):
        bfile.write(name + "\n")
    else:
        otherfile.write(name + "\n")

afile.close()
bfile.close()
otherfile.close()

##### CL4.5: Boolean operator (in this example 'or')
import csv
### Given the file, drosphila.csv, write a function called 'get_gene()' that takes in the data file. Write a loop that iterates through the rows and filter out the gene names that belong to Drosophila melanogaster or Drosophila simulans. Returns the values to a new list 'Dm_Ds'
### drosphila.csv's line is separated by ',' and consists of species, sequence, names, expression

### step 1: import library csv and read in file
import csv

### step 2: Iterate through each line and split string into different variables
with open('drosphila.csv', "r") as drosphila_file:
    data = csv.reader(drosphila_file)
    
    for line in data:
        species = line[0]
        sequence = line[1]
        name = line[2]
        expression = line[3]
        if species == "Drosophila melanogaster" or species == "Drosophila simulans":
            print(name)

