import re 


def open_file():
  #going to open file and clean up data
  with open('./inputs/day3.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

def move_toboggan(right, file):
  #takes number of spaces to move right per line
  #then checks for collision with tree (marked as '#')
  index = 0
  collisions = 0
  skip_first = 0
  
  for line in file:
    #increment index by number of spaces right per iteration
   
    if skip_first == 0:
      skip_first += 1
      index += right
    else:
      #there are 31 characters per line, find modulo when it wraps.
      position = (index % 31) 
      #print(f'position = {position}')
      #print(line)
      index += right
      if line[position] == '#':
        collisions += 1
        #print(f'collision detected on line {skip_first}, position {position}')

    
  print(collisions) 
    
move_toboggan(3, open_file())