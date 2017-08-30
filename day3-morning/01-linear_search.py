#!/usr/bin/env python

# Make the "random" library accessible in this script
import random

# Choose a random integer between 1 and 100, inclusive
r = random.randint(1,100)
print r


# Use a for loop to choose 50 random numbers
nums = []

for i in range(50):
	r = random.randint(1,100)
	print "The %dth number is %d" % (i, r)
	nums.append(r)

print "List of random numbers", nums

# Python has a sort() method to very quickly sort it
nums.sort()
print "Sorted list", nums

# Linear search
## Define some 'key' that we are going to search for in 'nums'
key = 42

## Check if the key is in our list of numbers
for i in range(len(nums)):
	v = nums[i]
	print "Scanning: the %dth number is %d" % (i, v)
	if v == key:
		print "*** Found it at position %d ***" % (i)
