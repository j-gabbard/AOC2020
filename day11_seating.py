import itertools
current = []
after = []
counter = 0

def open_file():
  #going to open file and clean up data
  with open('./inputs/day11.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]
    #ordered = sorted(scrubbed)
    return scrubbed

current = open_file()

#notes - 93 per line; indices 0-92

def get_neighbors(y, x):
  global current
  
  neighbors = 0
  #horizontal neighbors
  if x - 1 >= 0:
    if current[y][x-1] == '#':
      neighbors += 1
  if x + 1 <= len(current[0]) -1:
    if current[y][x+1] == '#':
      neighbors += 1
  
  #vertical/diagonal
  
  for xoffset in [-1, 0, 1]:
    for yoffset in [-1, 1]:
      if (
        x + xoffset >= 0 and x + xoffset <= len(current[0]) -1
        and y + yoffset >= 0 and y + yoffset <= len(current) - 1
      ):
        if current[y+yoffset][x+xoffset] == '#':
          neighbors += 1

  return neighbors
  
#print(get_neighbors(0, 3, open_file()))

def generate_after():
  global current
  global after
  row_counter = -1
  after = []
  for row in current:
    row_counter += 1
    seat_counter = 0
    queue = ''
    
    for seat in row:
      #print(row_counter, seat_counter)
      #hold_on = input()
      if seat == 'L' and get_neighbors(row_counter, seat_counter) == 0:
        queue += '#'
     
      
      elif seat == '#' and get_neighbors(row_counter, seat_counter) >= 4:
        queue += 'L'
      
      else:
        queue += seat
      seat_counter += 1
    
    after.append(queue)
      
def count_final():
  global current
  global after
  global counter
  
  generate_after()
  
  if current != after:
    current = after
    counter += 1
    print(f'iterations = {counter}')
    count_final()
  
  else:
    print(sum([row.count('#') for row in after]))
    print('program over')
################## part 2 below ##################  
def get_neighbors2(y, x):
  global current
  neighbors = 0
  xmax = len(current[0]) - 1
  ymax = len(current) - 1
  
  row = current[y]
  column = ''.join([current[i][x] for i in range(0, ymax + 1)])
  diag1 = '' #up-left
  diag2 = '' #down-right
  diag3 = '' #down-left
  diag4 = '' #up-right
  
  flags = {}
  for i in range(1,9):
    flags[i] = 0
  
  #these long-ass whiles aren't necessary for every component, but, lazy
  xoffset, yoffset = -1, -1
  while y + yoffset >= 0 and y + yoffset <= ymax and x + xoffset >= 0 and x + xoffset <= xmax:
    diag1 += current[y + yoffset][x + xoffset]
    xoffset -= 1
    yoffset -= 1    
  
  xoffset, yoffset = 1, 1
  while y + yoffset <= ymax and x + xoffset <= xmax:
    diag2 += current[y + yoffset][x + xoffset]
    xoffset += 1
    yoffset += 1
    
  xoffset, yoffset = -1, 1
  while y + yoffset >= 0 and y + yoffset <= ymax and x + xoffset >= 0 and x + xoffset <= xmax:
    diag3 += current[y + yoffset][x + xoffset]
    xoffset -= 1
    yoffset += 1
    
  xoffset, yoffset = 1, -1
  while y + yoffset >= 0 and y + yoffset <= ymax and x + xoffset >= 0 and x + xoffset <= xmax:
    diag4 += current[y + yoffset][x + xoffset]
    xoffset += 1
    yoffset -= 1
  

  for i in reversed(row[:x]):
    print(f'reversed row{i}')
    #hold_up = input()
    if i != '.':  
        if i == '#':
          flags[1] = 1
          neighbors += 1
        break  
        
  if x < xmax:
    for i in row[x+1:]:
      if i != '.':
        if i == '#':
          flags[2] = 1
          neighbors += 1
        break
        

  for i in reversed(column[:y]):
    print(f'reversed column{i}')
    #hold_up = input()
    if i != '.':  
        if i == '#':
          flags[3] = 1
          neighbors += 1
        break  
  if y < ymax:
    for i in column[y+1:]:
      if i != '.':
        if i == '#':
          flags[4] = 1
          neighbors += 1
        break
        
  
  for direction in [diag1, diag2, diag3, diag4]:
    for i in direction:
      if i != '.':
        if i == '#':
          neighbors += 1
        break
  
  print(f'row = {row}\n',
    f'column = {column}\n',
    f'diag1 = {diag1}\n',
    f'diag2 = {diag2}\n',
    f'diag3 = {diag3}\n',
    f'diag4 = {diag4}\n'
    )
  print(neighbors)
  print(flags.items())
  return neighbors
  
def generate_after2():
  global current
  global after
  row_counter = -1
  after = []
  for row in current:
    row_counter += 1
    seat_counter = 0
    queue = ''
    
    for seat in row:
      print(row_counter, seat_counter, seat)
      #hold_on = input()
      #print(get_neighbors2(row_counter, seat_counter))
      #hold_on = input()
      if seat == 'L' and get_neighbors2(row_counter, seat_counter) == 0:
        queue += '#'
     
      
      elif seat == '#' and get_neighbors2(row_counter, seat_counter) >= 5:
        queue += 'L'
      
      else:
        queue += seat
      seat_counter += 1
    
    after.append(queue)
        
  
def count_final2():
  global current
  global after
  global counter
  
  generate_after2()
  print([row for row in after])
  hold_on = input()
  if current != after:
    current = after
    counter += 1
    print(f'iterations = {counter}')
    count_final2()
  
  else:
    print(sum([row.count('#') for row in after]))
    print('program over')
    
count_final2()