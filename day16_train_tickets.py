import time
import re
import itertools
import math

mem = {}

def open_file():
  #going to open file and clean up data
  with open('./inputs/day16.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return scrubbed

def generate_data(inp):
  output = {}
  for line in inp:
    if 'or' in line:
      #split input into field and value, sanitize
      field, values = line.split(': ')
      field = '_'.join(field.split(' '))
      values = values.split(' or ')
      
      #assign each range to a variable
      range_low, range_high = [(x.split('-')) for x in values]
      
      #add that range to the valid list for that field
      value_list = []
      value_list.extend(range(int(range_low[0]), int(range_low[1]) + 1))
      value_list.extend(range(int(range_high[0]), int(range_high[1]) + 1))
      
      #add to dict
      output[field] = value_list
  
  return output
      

      

def find_invalid(inp):
  data = generate_data(open_file())
  #print(data)
  invalids = []
  valids = []
  for line in inp:
    if re.match(r'^[0-9]', line):
      numbers = [int(x) for x in line.split(',')]
      flag = 1
      for number in numbers:
        allowed = []
        for k, v in data.items():
          allowed.extend(v)
        if number not in allowed:
          invalids.append(number)
          flag = 0
      if flag == 1:
        valids.append(line)
  #print(sum(invalids))
  valids_out = []
  for x in valids:
    #valids_out.append(int(y) for y in x.split(','))
    temp = x.split(',')
    valids_out.append([int(y) for y in temp])
    #print(temp)
    #hold_on = input()
  #print(valids_out)
  return(valids_out)

ticket_fields = dict()
data = generate_data(open_file())


def find_categories_part_2(valid_tickets):
  global ticket_fields
  global data
  data1 = [x for x in data]

  
  #print(data)
  counter = 1
  while valid_tickets[0]: #using [0] since will contain a list of empty lists
    valid_field = [x.pop(0) for x in valid_tickets]
    #print(valid_tickets)
    #print(valid_field)
    #hold_on = input()
    uniques = []
    uniques.extend([x for x in valid_field if x not in uniques])
    flag = 0
    match = ''
    
    for k, v in data.items():
      #print(v)
      #print(set(uniques))
      #print(set(v))
      if set(uniques).issubset(v):
        #print(f'hay match - {counter} and {k}')
        match = k
        flag += 1
      
    if flag == 1:
      ticket_fields[counter] = match
      del data[match]
    
    counter += 1
    #print(counter)
  print(ticket_fields)
    
  if data:
    if data1 == data:
      print('nothing changed this time')
      exit()
    else:
      find_categories_part_2(find_invalid(open_file()))
    
      


  
  #print(valid_field)


def get_my_departure_product(my_ticket):
  global ticket_fields
  my_fields = []
  for k, v in ticket_fields.items():
    if re.match(r'^departure', v):
      my_fields.append(my_ticket[k - 1]) #started previous index at 1 for some reason
  
  print(my_fields)
  print(math.prod(my_fields))





t = time.time()
find_categories_part_2(find_invalid(open_file()))
get_my_departure_product([73,101,67,97,149,53,89,113,79,131,71,127,137,61,139,103,83,107,109,59])
#print(find_invalid(open_file()))
print(f'took {time.time()-t} seconds')
