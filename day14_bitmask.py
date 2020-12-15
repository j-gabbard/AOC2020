import time
import re
import itertools

mem = {}

def open_file():
  #going to open file and clean up data
  with open('./inputs/day14.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed


def bitmask(mask, inp):
  bin_inp = format(inp, 'b').zfill(36)
  temp = ''
  
  for index, digit in enumerate(bin_inp):
    if mask[index] == 'X':
      temp += digit
    elif mask[index] == '1':
      temp += '1'
    elif mask[index] == '0':
      temp += '0'
  return temp
  

def mem_mask(mask, address):
  temp = []
  output = []
  counter = 0
  bin_address = format(int(address), 'b').zfill(36)
  mask = mask.zfill(36)
    
  for index, digit in enumerate(bin_address):    
    if mask[index] == '1':
      temp.append('1')
    if mask[index] == 'X':
      temp.append('X')
      counter += 1
    elif mask[index] == '0':
      temp.append(digit)
  #need to convert back to a string
  temp = ''.join(temp)
  if counter == 0:
    return ''.join(temp)
    
  combos = list(itertools.product([0, 1], repeat=counter))
  
  for combo in combos:
    tempout = temp
    for x in combo:
      tempout = tempout.replace('X', str(x), 1)
    output.append(tempout)
  
  return output
  



def part1(inp):
  #apply bitwise mask to input value and write to memory address at index
  for line in inp:
    cmd, value = line.split(' = ')
    if cmd == 'mask':
      mask = value
    else:
      address = cmd[4:].split(']')[0]
      mem[address] = int(bitmask(mask, int(value)), 2)

  print(sum(mem.values()))

def part2(inp):
  #apply bitwise mask to memory address and write to masked address(es)
  #0 - bit unchanged
  #1 - bit written to 1
  #X - bit is "floating" and writes to both addresses
  for line in inp:
    cmd, value = line.split(' = ')
    if cmd == 'mask':
      mask = value
    if cmd.split('[')[0] == 'mem':
      masked = mem_mask(mask, cmd[4:].split(']')[0])
      for index in masked:
        mem[int(index, 2)] = int(value)
      continue
  
  print(sum(mem.values()))
  


  
t = time.time()
part1(open_file())  
part2(open_file())   
print(f'took {time.time()-t} seconds')
