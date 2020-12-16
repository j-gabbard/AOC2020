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
    





'''def add_nth_term(inp):
  #map number (index) to turn occurred (value)
  if inp[-1] in inp[:-2]:
    indices = [num for num, value in enumerate(inp) if value == inp[-1]]
    high = indices.pop(-1)
    low = indices.pop(-1)
    inp.append(high - low)
    return inp
    
  elif inp[-1] not in inp[:-2]:
    inp.append(0)
    return inp

def part2(inp):
  t = time.time()  
  counter2 = 1
  while len(inp) < 30000001:
    inp.append(add_nth_term(inp))
    counter2 += 1
    if counter2 % 1000 == 0:
      print(f'{counter2} took {time.time()-t} seconds')
  
  print(inp[29999999])'''
game = {1:10, 2:16, 3:6, 4:0, 5:1, 6:17}
#game = [[10, 0, 0], [16, 0, 1], [6, 0, 2]]
#10, 16, 6, 0, 1, 17, 0, 3, 0, 2, 0, 2, 2, 1, 
counter3 = 7
def part3(target):
  global game
  global counter3
  t = time.time()  

  while counter3 <= target:
  
    keys = game.keys()
    values = game.values()
    currentnum = game[max(keys)]
    #print(keys, values, currentnum)
    
    #check if the number already existed, delete lowest index, add next value
    #query = '\b
    #matches = re.findall(rfstr(currentnum), str(values))
    matches = sum([1 for x in values if x == currentnum])
    #print(matches)
    if matches >= 2:
      found = []
      oldest = 9999999999999
  
      for key, value in game.items():
        if value == currentnum:
          found.append(key)
          if key < oldest:
            oldest = key
      nextnum = abs(found[0] - found[1])
      del game[oldest]
      
    elif matches < 2:
      nextnum = 0
    
    
    game[counter3] = nextnum
    counter3 += 1
    #print(game.items())
    #hold_up = input()
    
    if counter3 % 10000 == 0:
      print(f'{counter3} took {time.time()-t} seconds')
  
  print(game[target])

game2 = {10:(0, 1), 16:(0, 2), 6:(0, 3), 0:(0, 4), 1:(0, 5), 17:(0, 6)}
#10, 16, 6, 0, 1, 17, 0, 3, 0, 2, 0, 2, 2, 1, 
  
def part4(target):
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
    
    #print('before', index, last_number, current_number, low, high, game2)
    #hold_on = input()


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
  
#part4(2020)      
part4(30000000)    
    
    
  