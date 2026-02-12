### This template is for the class demo and exercises covered in M02_L06_regular-exp for CS 22B.

### Import regular expression library
import re

##### CL6.1 Demonstrate regular expression
regexp = re.compile("Good luck, babe")
file = open("goodluck_babe.txt", "r")
count = 0
for line in file.readlines():
     if regexp.search(line):
         count = count + 1
file.close()
print(count)

## How do we capture "good luck, babe" and "Good luck, babe"?



##### CL6.3 Capturing groups in regex
seq = "ATGACGTACGTACGACTG"

matching = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", seq)
#print("entire match: " + matching.group())
#print("first bit: " + matching.group(1))
#print("second bit: " + matching.group(2))

##### CL6.4
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
#print("group one start: " + str(matching.start(1)))
#print("group one end: " + str(matching.end(1)))

##### CL6.5
accession = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

## Part A: contain the letters d and e in that order

## Part B: contain both the letters d and e in any order

## Part C: start with x or y and end with e

## Part D: contain three or more numbers in a row

## Part E: end with d followed by either a, r or p

