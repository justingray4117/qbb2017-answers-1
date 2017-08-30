#!/usr/bin/env python

# Binary Search

## Create a list of numbers, and define a key to search for 
## in that list
nums = range(0,100,10)
key = 0

## Inititialize the range to be searched as being the whole 
## list
lo = 0
hi = len(nums)

while lo < hi:
	## Find the middle item
	mididx = (lo + hi) / 2
	mid = nums[mididx]

	print "checking in the range [%d, %d], nums[%d]==%d" % (lo, hi, mididx, mid)

	## Compare the middle item to the list
	if (mid == key):
		print "Hooray! Found it at %d" % (mididx)
		break
	elif (key > mid):
		lo = mididx + 1
	else:
		hi = mididx
