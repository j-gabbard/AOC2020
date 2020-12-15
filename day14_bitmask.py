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

#print(open_file())

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
  #print(f'len(mask) = {len(mask)}, len(input) = {len(bin_inp)}, len(out) = {len(temp)}')
  return temp
  
#print(bitmask('11X00100011111110000X1010X001X010000', 101))

def mem_mask(mask, address):
  off = []
  on = []
  temp = []
  output = []
  counter = 0
  bin_address = format(int(address), 'b').zfill(36)
  mask = mask.zfill(36)
  
  print(bin_address, mask)
  
  for index, digit in enumerate(bin_address):    
    if mask[index] == '1':
      temp.append('1')
    if mask[index] == 'X':
      temp.append('X')
      counter += 1
    elif mask[index] == '0':
      temp.append(digit)
    print(mask[index], temp[-1])
  print(temp)
  #need to convert back to a string
  temp = ''.join(temp)
  print(len(temp), temp)
  if counter == 0:
    return ''.join(temp)
    
  combos = list(itertools.product([0, 1], repeat=counter))
  
  #print(combos)
  for combo in combos:
    tempout = temp
    for x in combo:
      tempout = tempout.replace('X', str(x), 1)
    #print(tempout)
    output.append(tempout)
  
  #print(bin_address, temp)
  print(output)
  return output
  
mem_mask('000000000000000000000000000000X1001X', '42')



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
      #print(masked)
      for index in masked:
        mem[int(index, 2)] = int(value)
      continue
  
  print(sum(mem.values()))
  
  
  
  #print(masked)
  
  
t = time.time()
#part1(open_file())  
part2(open_file())   
print(time.time()-t)
