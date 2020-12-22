import time
import re
import itertools
import sys

def open_file():
  #going to open file and clean up data
  with open('./inputs/day18.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def add(inp1, inp2):
  return inp1 + inp2
  
def multiply(inp1, inp2):
  return inp1 * inp2 

def part1(inp):
  output = []
  find_paren = re.compile(r'\([0-9\+\*\s]*\)')

  for line in inp:
    while re.search(find_paren, line):
      paren = re.search(find_paren, line).group(0).split(' ')
      paren_innards = [re.sub(r'(\(|\))', '', x) for x in paren]
      #check for multiple terms in parentheses and evaluate until empty
      while len(paren_innards) > 2:
        if paren_innards[1] == '+':
          new = int(paren_innards[0]) + int(paren_innards[2])
        
        elif paren_innards [1] == '*':
          new = int(paren_innards[0]) * int(paren_innards[2])
                
        paren_innards[2] = new
        del paren_innards[:2] #this sequence is sus as hell
  
      line = re.sub(find_paren, str(paren_innards[0]), line, count=1)
    
    #now all parentheses should be gone, time to work left-to-right
    x = line.split(' ')
    while len(x) > 2:
      if x[1] == '+':
        new = int(x[0]) + int(x[2])
          
      elif x[1] == '*':
        new = int(x[0]) * int(x[2])
          
      x[2] = new
      del x[:2] #reusing sus syntax but whatev
  
    output.append(int(x[0]))
  
  print(sum([i for i in output]))  
          
def part2(inp):
  output = []
  find_paren = re.compile(r'\([0-9\+\*\s]*\)')

  for line in inp:
    while re.search(find_paren, line):
      paren = re.search(find_paren, line).group(0).split(' ')
      paren_innards = [re.sub(r'(\(|\))', '', x) for x in paren]
      #check for multiple terms in parentheses and evaluate until empty
      while len(paren_innards) > 2:
        if '+' in paren_innards:
          idx = paren_innards.index('+')
          new = int(paren_innards[idx-1]) + int(paren_innards[idx+1])
          paren_innards[idx] = new
          del paren_innards[idx+1]
          del paren_innards[idx-1]
          
        elif paren_innards [1] == '*':
          new = int(paren_innards[0]) * int(paren_innards[2])
          paren_innards[2] = new
          del paren_innards[:2] #this sequence is sus as hell
      
      line = re.sub(find_paren, str(paren_innards[0]), line, count=1)
    #now all parentheses should be gone, time to work left-to-right
    x = line.split(' ')
    while len(x) > 2:
      if '+' in x:
        idx = x.index('+')
        new = int(x[idx-1]) + int(x[idx+1])
        x[idx] = new
        del x[idx+1]
        del x[idx-1]
        
      elif x[1] == '*':
        new = int(x[0]) * int(x[2])

        x[2] = new
        del x[:2] #this sequence is sus as hell
    output.append(int(x[0]))
  
  print(sum([i for i in output]))  
  
t = time.time()
part1(open_file())
part2(open_file())
print(f'took {time.time()-t} seconds')