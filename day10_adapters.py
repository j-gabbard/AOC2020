def open_file():
  #going to open file and clean up data
  with open('./inputs/day10.txt', 'r') as f:
    scrubbed = [int(x.strip()) for x in f.readlines()]
    ordered = sorted(scrubbed)
    return ordered
    
def part1(inp):
  delta1 = 0
  delta3 = 1 #providing jump start for last hop to device
  current = 0
  
  while inp:
    for adapter in inp:
        previous = current
        current = inp.pop(0)
        if current - previous == 1:
          delta1 += 1
        if current - previous == 3:
          delta3 += 1

  
  print(delta1 * delta3)
  
#part1(open_file())

def part2(inp):
  com = 1 #combinations
  req = [] #required
  
  for number in inp:
    if number + 1 not in inp and number + 2 not in inp and number not in req:
      req.append(number)
    if number - 1 not in inp and number - 2 not in inp and number not in req:
      req.append(number)

  counter = 0
  for number in req:
    #print(f'com = {com}, number = {number})')
    #hold_up = input()
    counter += 1
    intermediates = sum([1 for x in inp if x > number and x < req[counter]])
    if intermediates == 1:
      com *= 2
    if intermediates == 2:
      com *= 4
    if intermediates == 3:
      com *= 7
  
  print(com)

      
part2(open_file())

'''
* if there are no numbers +/- 2 next to a number, it is required
* if two numbers are separated by 4, 

6, 7, 8, 9, 10
6, 8, 9, 10
6, 9, 10
6, 7, 8, 10
6, 7, 9, 10
6, 7, 10
6, 8, 10  

If 3 intermediates, there are 7 combinations. Would be 2 ** 3 but one is necessary to keep distance <= 3. 
If 2 intermediates, there are 2 ** 2 combinations
If 1 intermediate, there are 2 ** 1 combinations
If 0 intermediates, only 2 ** 0 combinations, no change
'''


'''to test max difference between entries in "req" - this could be arbitrarily high
  test_max = 0
  test_counter = 0
  for number in req:
    test_counter += 1
    if test_counter < len(req):
      if req[test_counter] - number > test_max:
        test_max = req[test_counter] - number
  
  print(test_max)'''