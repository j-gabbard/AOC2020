import re 


def open_file():
  #going to open file and clean up data
  with open('./inputs/day9.txt', 'r') as f:
    text = f.readlines()
    scrubbed = [int(x.strip()) for x in text]
    #for line in f:
      #scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed


def part1(inp):
  
  while inp:
    flag = 0
    sliced = inp[:26]
    counter = 0
    for number in sliced:
      #print(number)
      #print(sliced)
      #print(sliced[25])
      
      #x = input()     
      if sliced[25] - number in sliced: 
        flag = 1
        inp.pop(0)
      
      if flag == 1:
        part1(inp)
      
      else:
        counter += 1
        if counter >= 24:
          print(f'might be a prob with {inp[25]}')

        
        
#part1(open_file())

def part2(inp):
  total, counter, first, smallest, largest = 0, 0, 0, 0, 0

  
  for number in inp:
    if counter == 0:
      first = number
    
    total += number
    counter += 1
    if number > largest:
      largest = number
    
    if smallest == 0:
      smallest = number
      
    if number < smallest:
      smallest = number
    
    if total > 32321523:
    #if total > 127:
      inp.pop(0)
      part2(inp)
    
    
    if total == 32321523 and counter > 1:
    #if total == 127 and counter > 1:
      print(f'first = {first}, last = {number}')
      print(f'smallest = {smallest}, largest = {largest}')
      print(f'sum = {smallest + largest}')
      
part2(open_file())
    