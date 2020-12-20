import time
import re
import itertools
import sys

sys.setrecursionlimit(2200)

#game = {10: [0], 16:[1], 6:[2], 0:[3], 1:[4], 17:[5]}
game = [10,16,6,0,1,17]
counter = 0


def open_file():
  #going to open file and clean up data
  with open('./inputs/day14.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def part1(inp):
  #map number (index) to turn occurred (value)
  global counter
 #print(inp)
 #print(inp[-1])
 #print(inp[:-2])
  if counter < 2021:
    if inp[-1] in inp[:-2]:
      indices = [num for num, value in enumerate(inp) if value == inp[-1]]
      high = indices.pop(-1)
      low = indices.pop(-1)
      counter += 1
      inp.append(high - low)
      part1(inp)
    
    elif inp[-1] not in inp[:-2]:
      counter += 1
      inp.append(0)
      part1(inp)
  
  if counter > 2019:
    return(inp[2020 - 1])
    


game2 = {10:(0, 1), 16:(0, 2), 6:(0, 3), 0:(0, 4), 1:(0, 5), 17:(0, 6)}
  
def part2(target):
#less slow way to do the thing 
  global game2
  index = 7
  last_number = 17
  current_number = 999
  uniques = [10, 16, 6, 0, 1, 17]
  t = time.time()
  
  while index <= target:
    numbers = game2.keys()
    indices = game2.values()
    high = game2[last_number][1]
    low = game2[last_number][0]
    
    if low == 0:
      current_number = 0
      
    elif low != 0:
      current_number = high - low
      
    if current_number not in uniques:
      uniques.append(current_number)
      game2[current_number] = (0, index)
    
    elif current_number in uniques:
      game2[current_number] = (game2[current_number][1], index)
            
    last_number = current_number
    index += 1
    if index % 10000 == 0:
      print(f'{index} took {time.time()-t} seconds')    

  print(f'the {target}th number is {last_number}')
  
#part2(2020)      
part2(30000000)    
    
    
  