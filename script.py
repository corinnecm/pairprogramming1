# Save arg names as variables
from sys import argv
from collections import defaultdict

if __name__ == '__main__':
    source1 = argv[1]
    source2 = argv[2]
    out_name = argv[3]

def function1(source1, source2):
    source1_d = defaultdict(list)
    with open(source1, 'r') as source1file:

# Create two default dicts for each review source

# Go through each line in each file and add each review score to the default dict.

# Alphabetically sort by restaurant name

# Write a file that has restaurant name, avg1, avg2
