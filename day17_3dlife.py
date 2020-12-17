import time
from itertools import product

def open_file():
  #going to open file and clean up data
  with open('./inputs/day17.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def parse_input():
  inp = open_file()
  counter = 0
  on, off = [], []
  cells = dict()
  x_count = range(-20, 20)
  y_count = range(-20, 20)
  z_count = range(-10, 10)
  
  cubes = (product(x_count, y_count, z_count))
  for cube in cubes:
    cells[cube] = 0
    
  
  
  for line in inp:
    for index, character in enumerate(line):
      if character == '#':
        cells[(index, counter, 0)] = 1
      elif character == '.':
        cells[(index, counter, 0)] = 0
    counter += 1
    return cells
  
def check_neighbors(xyz, inp):
  #xyz = x, y, z coordinates of cell as tuple
  #inp = dict of cells
  x_neighbors = range(xyz[0] - 1, xyz[0] + 2) #+ 2 because of how range works
  y_neighbors = range(xyz[1] - 1, xyz[1] + 2)
  z_neighbors = range(xyz[2] - 1, xyz[2] + 2)
  on = 0
  
  nearby = list(product(x_neighbors, y_neighbors, z_neighbors))
  for neighbor in nearby:
    if neighbor in inp:
      if inp[neighbor] == 1:
        on += 1

  if inp[xyz] == 1:
    on -= 1 #need to un-count itself 
  return on
  
def peer_into_future(cycles):
  staten = parse_input()
  counter = 0

  for counter in range(1, 7):
    staten1 = dict()
    total = 0
    
    for cell in staten:
      nei = check_neighbors(cell, staten)
      if(nei == 2 or nei == 3) and staten[cell] == 1:
        staten1[cell] = 1 #cell lives if just enough neighbors
        total += 1
      
      elif(nei < 2 or nei > 3) and staten[cell] == 1:
        staten1[cell] = 0 #cell dies if not enough or too many neighbors
     
      elif nei == 3 and staten[cell] == 0:
        staten1[cell] = 1 #cell revives if exactly 3 neighbors
        total += 1
        
      elif nei != 3 and staten[cell] ==0:
        staten1[cell] = 0 #cell stays dead if not 3 neighbors
        
    counter += 1
    staten = staten1
    del staten1
    
    print(f'cycles done: {counter}, total = {total}')
    
 
####################################################################################
 
def parse_input4():
  inp = open_file()
  counter = 0
  on, off = [], []
  cells = dict()
  x_count = range(-10, 15)
  y_count = range(-10, 15)
  z_count = range(-7, 7)
  w_count = range(-7, 7)
 
  cubes = (product(x_count, y_count, z_count, w_count))
  for cube in cubes:
    cells[cube] = 0
    
  #print(cells)
  
  
  for line in inp:
    for index, character in enumerate(line):
      if character == '#':
        cells[(index, counter, 0, 0)] = 1
      elif character == '.':
        cells[(index, counter, 0, 0)] = 0
    counter += 1
  
  #print(on, off)
  return cells
  
def check_neighbors4(xyzw, inp):
  #xyz = x, y, z, w coordinates of cell as tuple
  #inp = dict of cells
  x_neighbors = range(xyzw[0] - 1, xyzw[0] + 2) #+ 2 because of how range works
  y_neighbors = range(xyzw[1] - 1, xyzw[1] + 2)
  z_neighbors = range(xyzw[2] - 1, xyzw[2] + 2)
  w_neighbors = range(xyzw[3] - 1, xyzw[3] + 2)
  on = 0
  
  nearby = list(product(x_neighbors, y_neighbors, z_neighbors, w_neighbors))
  for neighbor in nearby:
    if neighbor in inp:
      if inp[neighbor] == 1:
        on += 1
      
  if inp[xyzw] == 1:
    on -= 1 #need to un-count itself 
  return on
  
def peer_into_future4(cycles):
  staten = parse_input4()
  counter = 0
  while counter < cycles:
    staten1 = dict()
    #print(staten)
    total = 0
    for cell in staten:
      nei = check_neighbors4(cell, staten)
      if (nei == 2 or nei == 3) and staten[cell] == 1:
        staten1[cell] = 1 #cell lives if just enough neighbors
        total += 1
      
      elif (nei < 2 or nei > 3) and staten[cell] == 1:
        staten1[cell] = 0 #cell dies if not enough or too many neighbors
     
      elif nei == 3 and staten[cell] == 0:
        staten1[cell] = 1 #cell revives if exactly 3 neighbors
        total += 1
        
      elif nei != 3 and staten[cell] ==0:
        staten1[cell] = 0 #cell stays dead if not 3 neighbors
        
    counter += 1
    staten = staten1
    del staten1
    
    print(f'cycles done: {counter}, total = {total}')
  
      
t = time.time()
#peer_into_future(6)
peer_into_future4(6)
print(f'took {time.time()-t} seconds')
