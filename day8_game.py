import re 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day8.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

def part1(inp):
  #Starts at first assembly instruction and evaluates it
  acc = 0
  position = 0
  executed = []
  
  while position not in executed:
    #check position to make sure not out of range
    if position > len(inp) - 1:
      return position, acc
    
    else:
    
      #check to make sure we haven't run the instruction
      command, value = inp[position].split(' ')
      if command == 'acc':
        #increment accumulator and go on to next command
        acc += int(value)
        executed.append(position)
        position += 1
          
      elif command == 'jmp':
        #jump command to given position
        executed.append(position)
        if position + int(value) > len(inp):
          return position, acc
        else: position += int(value)
          
      elif command == 'nop':
        #go to next instruction
        executed.append(position)
        position += 1
  

  #print(f'part 1 end {position}, {command}, {value}')
  return position, acc
      


def change_line(line):
  inp = open_file()
  buffer = inp
  command2, value2 = inp[line].split(' ')
  
  #check for jmp, swap to nop, look for result > 600
  if command2 == 'jmp':
    buffer[line] = f'nop {value2}'
    result = part1(buffer)
    if result[0] > 600:
      print(f'look at position {result[0]}, acc {result[1]}')

  if command2 == 'nop':
    buffer[line] = f'jmp {value2}'
    result = part1(buffer)
    if result[0] > 600:
      print(f'look at position {result[0]}, acc {result[1]}')
    
print(part1(open_file()))
for i in range(0,620):
  change_line(i)

    
