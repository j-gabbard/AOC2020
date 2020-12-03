import re 
product = 1

def open_file():
  #going to open file and clean up data
  with open('./inputs/day3.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

def move_toboggan(right, down, file):
  #takes number of spaces to move right per line
  #then checks for collision with tree (marked as '#')
  index = 0
  collisions = 0
  line_count = 0
  
  
  for line in file:
    #increment index by number of spaces right per iteration
   
    if line_count == 0:
      line_count += 1
      index += right
      #print(line)
    elif line_count % down == 0:
      #there are 31 characters per line, find modulo when it wraps.
      position = (index % 31) 
      #print(f'position = {position}')
      #print(line)
      index += right
      line_count += 1
      if line[position] == '#':
        collisions += 1
        #print(f'collision detected on line {line_count}, position {position}')
    else:
      line_count += 1
      #print(line)
      continue
    
  return collisions 
    
#print(move_toboggan(1, 1, open_file()))
#print(move_toboggan(3, 1, open_file()))
#print(move_toboggan(5, 1, open_file()))
#print(move_toboggan(7, 1, open_file()))
#print(move_toboggan(1, 2, open_file()))

product *= move_toboggan(1, 1, open_file())
product *= move_toboggan(3, 1, open_file())
product *= move_toboggan(5, 1, open_file())
product *= move_toboggan(7, 1, open_file())
product *= move_toboggan(1, 2, open_file())

print(f'product of all is {product}') 
