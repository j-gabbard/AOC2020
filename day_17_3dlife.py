import time
import re
import math
import timeit 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day17.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def parse_input():
  inp = open_file()
  on, off = []
  counter = 0
  for line in inp:
    for index, character in enumerate(line):
      if character == '#':
        on.append((index, counter, 0))
      elif character == '.':
        off.append((index, counter, 0))
  
  print(on, off)
        




t = time.time()
find_categories_part_2(find_invalid(open_file()))
get_my_departure_product()
print(f'took {time.time()-t} seconds')
