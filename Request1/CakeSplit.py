from __future__ import division
import math
#import pprint as pp
#test_strings = ["sdghdfghdfgbdfsvretgfertvbr","adsfbhadsfbhadsfbhadsfbhadsfbhadsfbhadsfbhadsfbhadsfbhadsfbhadsfbh","","a","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaa","adesadesadesades"]

def answer(s):
  fair_splits = fairSplits(s)
#  print "Any of these will be fair"
#  print fair_splits
#  print "However the most fairest cake of them all is "+str(fair_splits[0])
  return fair_splits[0]

def possibleSlices(s):
  len_s = len(s)
  sqrt_len_s = math.sqrt(len_s)
  factors_len_s = []
#  print "Square Root of Length: "+str(sqrt_len_s)
  is_factor = 1
  while is_factor < sqrt_len_s:
    is_factor_pair = len_s/is_factor
#    print "Testing Factor " + str(is_factor) + " and Factor Pair " + str(is_factor_pair)
    if len_s % is_factor == 0:
      insert_at = int(len(factors_len_s)/2)
      factors_len_s.insert(insert_at,int(is_factor_pair))
      factors_len_s.insert(insert_at,int(is_factor))
#      print "Pair is a Factor"
#    else:
#      print "Factor is not a Pair"
    is_factor += 1
  if sqrt_len_s % 1 == 0:
#    print "Square root "+str(sqrt_len_s)+" is a factor of the length"
    factors_len_s.insert(int(len(factors_len_s)/2),int(sqrt_len_s))
#    print "Cake of size "+ str(len_s) + " can be cut into these # of slices"
#    print factors_len_s
  return factors_len_s
    
def fairSplits(s):
  possible_slices = possibleSlices(s)
  fair_splits = []
#  print "The cake to test is " + s
  for index in range(len(possible_slices)):
#    print "Running Test Number "+str(index)
    test_num_slices = possible_slices[-(index+1)]
    test_slice = s[:possible_slices[index]]
#    print "Testing "+str(test_num_slices)+" number of slices"
    cake_of_slices = test_num_slices*test_slice
#    print "Cake is done ======> "+cake_of_slices
    if cake_of_slices == s:
##      print "A cake of "+str(test_num_slices)+" will be fair!!!"
      fair_splits.append(test_num_slices)
  return fair_splits
  
	
#for test_string in test_strings:
#  answer(test_string)
