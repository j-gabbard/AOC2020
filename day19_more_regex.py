import time
import re
import itertools
import sys

def open_file():
  #going to open file and clean up data
  with open('./inputs/day19.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def make_regex_dict_and_test_inputs(inp):
  regex_dict = dict()
  for line in inp:
    if ':' in line:
      x, y = line.split(': ')
      regex_dict[x] = y
    
  strings = [i for i in inp if re.search(r'^[ab]+', i)]
  return regex_dict, strings
      

  
def concatenate_regex(start):
  rules, strings = make_regex_dict_and_test_inputs(open_file())
  #print(rules)
  
  output = rules[start]
  looking = re.compile(r'\b[0-9]+\b')

  while re.search(looking, output):
    
    match = re.search(looking, output).group(0)
    output = re.sub(looking, f'({rules[match]})', output, count=1)
    
    #print(output)
    #print(re.search(looking, output))
    #hold_up = input()
    
  #print(output)
  output1 = re.sub(r'a\)', 'a', output)
  output2 = re.sub(r'\(b\)', 'b', output1)
  print(re.sub(r'(\s|\")', '', output2))
  return(re.sub(r'(\s|\")', '', output))

def find_matches():
  dictionary, strings = make_regex_dict_and_test_inputs(open_file())
  regex = re.compile(concatenate_regex('0'))
  counter = 0
  print(regex)
  
  for line in strings:
    if re.search(str(line), str(regex)):
      counter += 1
      
  print(counter)

find_matches()

#print([line.split(': ') for line in open_file()])

t = time.time()
print(f'took {time.time()-t} seconds')