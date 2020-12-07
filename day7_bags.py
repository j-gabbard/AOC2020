import re 
valid = 0
valid_list = ['shiny gold']
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
    
    outer.append(outer1)
    inner.append(inner1)
  
  bag_dict = dict(zip(outer, inner))
  #for k, v in bag_dict.items():
    #print(k, v)
 

def find_outers(colors):
  global bag_dict
  global valid_list
  #print(colors)
  done_check = len(valid_list)
  
  for k, v in bag_dict.items():
    #print(f'colors = {colors}, k = {k}, v = {k}')
    #hold_up = input()
    for color in colors:
      if color in v:
        #print(f'color = {color}, k = {k}, v = {v}')
        #hold_up = input()
        #temp_colors = re.sub(r'[0-9]\s', '', v).strip()
        valid_list.append(k)
        bag_dict[k] = ''
        #print(k, v)
  
  #print(valid_list)
  #hold_up = input()
  
  if done_check != len(valid_list):
    #sorted_list = sorted(
    print(sorted(list(set(valid_list))))
    hold_up = input()
    find_outers(valid_list)
  else:
    print(f'hopefully the total count is {len(set(valid_list))}')

    

generate_list(open_file())
find_outers(valid_list)