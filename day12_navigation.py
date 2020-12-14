import time
import re


def open_file():
  #going to open file and clean up data
  with open('./inputs/day12.txt', 'r') as f:
    temp = [x.strip() for x in f.readlines()]
    scrubbed = [x[0] + ' ' + x[1:] for x in temp]
    
    #ordered = sorted(scrubbed)
    return scrubbed

#print(open_file())

def part1(inp):
  x = 0
  y = 0
  direction = 0

  for instruction in inp:
    letter = instruction.split(' ')[0]
    amount = int(instruction.split(' ')[1])
    if letter == 'E':
      x += amount
    elif letter == 'N':
      y += amount
    elif letter == 'W':
      x -= amount
    elif letter == 'S':
      y -= amount
    elif letter == 'F':
      if direction % 360 == 0:
        x += amount
      elif direction % 360 == 90:
        y += amount
      elif direction % 360 == 180:
        x -= amount
      elif direction % 360 == 270:
        y -= amount 
    elif letter == 'R':
      direction -= amount
      while direction < 0:
        direction += 360
    elif letter == 'L':
      direction += amount
      while direction < 0:
        direction += 360
        
  print(abs(x) + abs(y))


def part2(inp):
  x = 0
  y = 0
  wayx = 10
  wayy = 1

  for instruction in inp:
    letter = instruction.split(' ')[0]
    amount = int(instruction.split(' ')[1])
    if letter == 'E':
      wayx += amount
    elif letter == 'N':
      wayy += amount
    elif letter == 'W':
      wayx -= amount
    elif letter == 'S':
      wayy -= amount
    
    elif letter == 'R':
      if amount % 360 == 90:
        tempx, tempy = wayx, wayy
        wayx, wayy = tempy, tempx * -1
      if amount % 360 == 180:
        wayx, wayy = wayx * -1, wayy * -1
      if amount % 360 == 270:
        tempx, tempy = wayx, wayy
        wayx, wayy = tempy * -1, tempx

    elif letter == 'L':
      if amount % 360 == 270:
        tempx, tempy = wayx, wayy
        wayx, wayy = tempy, tempx * -1
      if amount % 360 == 180:
        wayx, wayy = wayx * -1, wayy * -1
      if amount % 360 == 90:
        tempx, tempy = wayx, wayy
        wayx, wayy = tempy * -1, tempx
        
    elif letter == 'F':
      x += amount * wayx
      y += amount * wayy 
    

  print(abs(x) + abs(y))
  
part1(open_file())  
part2(open_file())
t = time.time()
part1(open_file())  
part2(open_file())   
print(time.time()-t)
