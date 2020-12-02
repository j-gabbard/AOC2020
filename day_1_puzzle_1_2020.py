import os

def open_file():
  #going to open file and clean up data
  with open('input.txt', 'r') as f:
    raw_numbers = f.readlines()
    fixed_numbers = []
    for number in raw_numbers:
      fixed_numbers.append(int(number.rstrip()))
    return fixed_numbers
  
def two_complement_finder(target, fixed_numbers):
  #finds product of two numbers that sum to target
  for number in fixed_numbers:
    #print(number)
    complement = (target - number)
    #print(complement)
    if complement in fixed_numbers:
      print(f'{number} and {complement}')
      print(f'Product is {number * complement}')
      return [number, complement]

two_complement_finder(2020, open_file())

def three_complement_finder(target, fixed_numbers):
  #finds product of three numbers that sum to target
  for number in fixed_numbers:
    complement3 = (target - number)
    if two_complement_finder(complement3, fixed_numbers):
      print(f'Number is {number}, and the complements are\n'
      f'{two_complement_finder(complement3, fixed_numbers)}\n')
      break
    
three_complement_finder(2020, open_file())
    