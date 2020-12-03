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
    #quantity is first part of line so easy to split
    quantity = line.split()[0].split('-')
    
    #get low/high for range(), remembering that upper range is not inclusive
    quantity_low = int(quantity[0])
    quantity_high = int(quantity[1]) + 1
    
    #print(quantity)
    #print(quantity_low)
    #print(quantity_high) 
    
    #need to get the character to match on and the password. Could have done 
    #split[1] but then have to clean up colon. Lookahead avoids this. 
    character = re.search('[a-z](?=[:])', line).group()
    password = line.split()[-1]
    
    for letter in password:
      if letter == character:
        character_counter += 1
    
    if character_counter in range(quantity_low, quantity_high):
      line_counter += 1

  print(line_counter)   
  
#password_check(open_file())

def password_check_v2(passwords):
  # given an input, make sure the character appears in exactly the low or
  # in the high quantity postion, not both. Search should find the nth
  # character, not index (no 0th character)
  
  line_counter = 0
  for line in passwords:
    character_counter = 0
    #quantity is first part of line so easy to split
    quantity = line.split()[0].split('-')
    #print(quantity)

    #need to get the character to match on and the password. Could have done 
    #split[1] but then have to clean up colon. Lookahead avoids this. 
    character = re.search('[a-z](?=[:])', line).group()
    password = line.split()[-1]
    
    #get low/high values, remembering to add 1 to both for 
    #index to character conversion - nth character is n-1 index
    
    position_low = int(quantity[0]) - 1
    position_high = int(quantity[1]) - 1
    flag = 0
    
    #print(character)
    #print(position_low)
    #print(position_high)
    
    try:
      if password[position_low] == character:
        flag += 1
    except IndexError:
      pass
    
    #print(flag)
    
    try:
      if password[position_high] == character:
        flag += 1
    except IndexError:
      pass
      
    #print(flag)
      
    #checking to make sure both weren't true
    if flag == 1:
      line_counter += 1

  print(line_counter)  

password_check_v2(open_file())
