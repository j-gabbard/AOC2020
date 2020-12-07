import re 
valid_list = ['1 shiny gold']
bags = []
bag_dict = {}


def open_file():
  #going to open file and clean up data
  with open('./inputs/day7.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed
  
def generate_list(data):
  global bag_dict
  outer = []
  inner = []

  for bag in data:
    outer1 = bag.split('contain')[0]
    inner1 = bag.split('contain')[1]
    
    outer1 = re.sub(r'bags', '', outer1).strip()
    inner1 = re.sub(r'(\sbag[s]?|\.$)', '', inner1).strip()

    outer.append(outer1)
    inner.append(inner1)
  
  bag_dict = dict(zip(outer, inner))

 

def find_outers(colors):
  global bag_dict
  global valid_list
  #print(colors)
  done_check = len(valid_list)
  
  for k, v in bag_dict.items():
    for color in colors:
      if color in v:
        valid_list.append(k)
        #can't delete entry during recursion; set value to null
        bag_dict[k] = ''

  
  if done_check != len(valid_list):
    #sorted_list = sorted(
    #print(sorted(list(set(valid_list))))
    #hold_up = input()
    find_outers(valid_list)
  else:
    print(f'hopefully the total count is {len(set(valid_list)) -1}')

generate_list(open_file())

def part2(colors):
  #this forms and loops through a queue, but recursion is hard and this doesn't work. 
  global valid_list
  global bag_dict
  calculation = ''
  
  while valid_list:
    temp = valid_list.pop(0)
    qty, color = temp.split(' ', 1)
    
    #print(qty, color)
    for k, v in bag_dict.items():
      if color in k:
        if 'no other' in v:
          calculation += ')'
          continue
        else:
          calculation += f'{qty}(' 
          for x in v.split(', '):
            valid_list.append(x)
            
      
  
  print(calculation)
  
part2(valid_list)


