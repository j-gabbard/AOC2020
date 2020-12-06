import re 

def open_file():
  #going to open file and clean up data
  with open('./inputs/day6.txt', 'r') as f:
    scrubbed = []
    lines = f.read().split("\n\n")
    scrubbed = [line.replace('\n','') for line in lines]

    return scrubbed

def sum_answers(input_data):
  #print(input_data)
  total_sum = 0
  #for group in input_data:
    #print(group)
  for group in input_data:
    yes_answers = []
    #print(group)
    #hold_on = input()      
    for answer in group:
      if answer not in yes_answers and answer != '\n':
        yes_answers.append(answer)
        #print(yes_answers)
        #x = input()
        total_sum += 1
  
  print(total_sum)

sum_answers(open_file())
