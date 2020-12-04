import re 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day4.txt', 'r') as f:
    scrubbed = []
    lines = f.readlines()
    scrubbed = ' '.join([line.strip() for line in lines]).replace('  ', '\n')

    return scrubbed


def check_passports(passports):
  #takes list of passports with values assigned as key:value and determines
  #whether all 7 necessary fields are present
  counter = 0 #master count of valid passports
  fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  
  for passport in passports.split('\n'):
    flag = 0
    #print(passport)
    for field in fields:
      if re.search(field, passport):
        flag += 1 #increment flag for each valid key, 7 valid means valid passport

      
    if flag == 7:
      sub_flag = 0
      byr_check = re.search(r'byr:[0-9]{4}\b', passport)
      iyr_check = re.search(r'iyr:[0-9]{4}\b', passport)
      eyr_check = re.search(r'eyr:[0-9]{4}\b', passport)
      hgt_check = re.search(r'hgt:[0-9]{2,3}(in|cm)\b', passport)
      hcl_check = re.search(r'hcl:#[0-9a-f]{6}\b', passport)
      ecl_check = re.search(r'ecl:[a-z]{3}\b', passport)
      pid_check = re.search(r'pid:[0-9]{9}\b', passport)
      
      if byr_check and iyr_check and eyr_check and hcl_check and ecl_check and pid_check and hgt_check:
        if int(byr_check.group().split(':')[1]) >= 1920 and int(byr_check.group().split(':')[1]) <= 2002:
          sub_flag += 1
        if int(iyr_check.group().split(':')[1]) >= 2010 and int(iyr_check.group().split(':')[1]) <= 2020:
          sub_flag += 1
        if int(eyr_check.group().split(':')[1]) >= 2020 and int(eyr_check.group().split(':')[1]) <= 2030:
          sub_flag += 1
        if hcl_check.group().split(':')[1]:
          sub_flag += 1
        if ecl_check.group().split(':')[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
          sub_flag += 1         
        if pid_check.group().split(':')[1]:
          sub_flag += 1
        if re.search('cm', hgt_check.group()):
          if re.search(r'[0-9]{3}', hgt_check.group()):
            hgt_cm = re.search(r'[0-9]{3}', hgt_check.group())
            if int(hgt_cm.group()) >= 150 and int(hgt_cm.group()) <= 193:
              sub_flag += 1 
        if re.search('in', hgt_check.group()):        
          if re.search(r':[0-9]{2}', hgt_check.group()):
            hgt_in = re.search(r'[0-9]{2}', hgt_check.group())
            if int(hgt_in.group()) >= 59 and int(hgt_in.group()) <= 76:
              sub_flag += 1
      
      if sub_flag == 7:
        counter += 1
     
              
  print(f'counter says {counter} passports are valid')

check_passports(open_file())