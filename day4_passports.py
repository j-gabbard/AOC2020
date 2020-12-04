import re 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day4.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

#open_file()

def check_passports(passports):
  #takes list of passports with values assigned as key:value and determines
  #whether all 7 necessary fields are present
  counter = 0 #master count of valid passports
  line_count = 0
  fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  flag = 0 #initial setting of 0
  
  for passport in passports:
    line_count += 1
    if passport == '':
      flag = 0 #set flag to 0 on any empty line
      continue
      
    for field in fields:
      if re.search(field, passport):
        flag += 1 #increment flag for each valid key, 7 valid means valid passport
        #print(re.search(field,passport).group())
        #print(f'flag = {flag}')
    
    if flag == 7:
      counter += 1
      print(f'Passport ending on line {line_count} is valid')
    
  
  print(f'counter says {counter} passports are valid')

check_passports(open_file())