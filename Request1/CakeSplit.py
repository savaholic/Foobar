#! /usr/bin/python
from __future__ import division
import math
import pprint as pp

def answer(s):
  max_slices = len(s)
  sqrt_max_slices = math.sqrt(max_slices)
  num_slices = 1
  while num_slices < sqrt_max_slices:
    if max_slices % num_slices == 0:
      slice_size = int(max_slices/num_slices)
#      print "Testing if either "+str(slice_size)+" or "+str(num_slices)+" are optimal splits"
#      Since num_slices makes a cake of even size. slice_size num of slices will make num_slices size slices of cake 
      if isFairSplit(s,s[:num_slices],slice_size):
        return slice_size
      elif isFairSplit(s,s[:slice_size],num_slices):
        most_fairest_slices = num_slices
    num_slices += 1
  if (sqrt_max_slices % 1 == 0) and (isFairSplit(s,s[:int(sqrt_max_slices)],int(sqrt_max_slices))):
    return int(sqrt_max_slices)
  else:
    return most_fairest_slices

def isFairSplit(s, test_slice, test_num_slices):
  cake_of_slices = test_num_slices*test_slice
  if cake_of_slices == s:
    return True
  else:
    return False
