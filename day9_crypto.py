import re 


def open_file():
  #going to open file and clean up data
  with open('./inputs/day9.txt', 'r') as f:
    text = f.readlines()
    scrubbed = [int(x.strip()) for x in text]
    return scrubbed


def part1(inp):
  
  while inp:
    flag = 0
    #get first 26 entries. The rest don't matter for this iteration
    sliced = inp[:26] 
    counter = 0
    
    for number in sliced:     
      #look in list for the other addend that makes 26th number
      #if it exists, pop first number and do it again
      if sliced[25] - number in sliced: 
        #flag = 1
        inp.pop(0)
        part1(inp)

      
      #if flag == 1:
      
      else:
        counter += 1
        if counter >= 24:
          return(f'might be a prob with {inp[25]}')
          exit()
        
        
print(part1(open_file()))

def part2(inp, target):
  #find contiguous range that adds to the number from part 1
  #returns the sum of smallest and largest numbers in that range
  
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
      
    if number < smallest or smallest == 0:
      smallest = number
    
    #total > target means no need to continue since no negative numbers. 
    #pop first value and start over. 
    if total > target:
      inp.pop(0)
      part2(inp, target)    
    
    if total == target and counter > 1:
      #print(f'first = {first}, last = {number}')
      #print(f'smallest = {smallest}, largest = {largest}')
      print(f'sum = {smallest + largest}')
      exit()
      
part2(open_file(), 32321523)
    