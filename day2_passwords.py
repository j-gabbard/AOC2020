import re 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day2.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

def password_check(passwords):
  for line in passwords:
    quantity = line.split()[0]
    character = re.search('[a-z](?=[:])', line).group()
    password = line.split()[-1]
    #print(quantity)
    #print(characterraw)
    #print(password)
    
password_check(open_file())
   