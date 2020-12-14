import time
import re
from functools import reduce


def open_file():
  #going to open file and clean up data
  with open('./inputs/day13test.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

print(open_file())

def part1(inp):
  target = int(inp[0])
  buses = [int(x) for x in inp[1].split(',') if x != 'x']
  minimum = 999999
  best_bus = '' 
  
  for x in buses:
    wait = x - (target % x)
    if wait < minimum:
      minimum = wait
      best_bus = x
      
  
  #print(target, buses, best_bus, minimum)
  print(best_bus * minimum)


def part2(inp):
  buses = [x for x in inp[1].split(',')]
  indexed_buses = []
  #print(buses)
  #for index, bus in enumerate(buses):
    #print(index, bus)
  product = 1
  for index, bus in enumerate(buses):
    if bus != 'x':
      product *= (int(bus) + index)
      indexed_buses.append(int(bus) + index)
  
  print(indexed_buses)
      
  
  #number = reduce(lambda x,y:x*y,[int(i) for i in buses if i != 'x'])
  print(product)
  start = 0
  flag = 0
  while flag < len(buses):
    timetable = range(start, start + len(buses))
    #print(timetable)
    flag = 0
    if start % 100000 == 0:
      print(start)
    for index, bus in enumerate(buses):
      #print(index, bus)
      if bus == 'x':
        flag += 1
        continue
      elif timetable[index] % int(bus) == 0:
        flag += 1
        continue
      else:
        start += int(buses[0])
        break
      
      print(timetable)
  print(start) 
      
    
t = time.time()
#part1(open_file())  
part2(open_file())   
print(time.time()-t)
