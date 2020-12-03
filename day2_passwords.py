import re 


def open_file():
  #going to open file and clean up data
  with open('./inputs/day2.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

'''def consecutive_password_check(passwords):
  counter = 0
  for line in passwords:
    quantity = line.split()[0].replace('-', ',')
    character = re.search('[a-z](?=[:])', line).group()
    password = line.split()[-1]
    regex = character + '{' + f'{quantity}' + '}' 

    
    results = re.search(rf'{regex}', password)
    if results:
      #print(results.group())
      counter += 1
    #print(regex)
    #print(quantity)
    #print(character)
    #print(password)
  print(counter)
  
    
password_check(open_file())'''


def password_check(passwords):
  line_counter = 0
  for line in passwords:
    character_counter = 0
    #quantity is last part of line
    quantity = line.split()[0]
    
    quantity_list = quantity.split('-')
    quantity_low = int(quantity_list[0])
    quantity_high = int(quantity_list[1]) + 1
    
    #print(quantity)
    #print(quantity_low)
    #print(quantity_high) 
    
    character = re.search('[a-z](?=[:])', line).group()
    password = line.split()[-1]
    regex = character + '{' + f'{quantity}' + '}' 
    
    for letter in password:
      if letter == character:
        character_counter += 1
    
    if character_counter in range(quantity_low, quantity_high):
      line_counter += 1

  print(line_counter)   
  
password_check(open_file())