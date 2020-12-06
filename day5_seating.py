import re 


def open_file():
  #going to open file and clean up data
  with open('./inputs/day5.txt', 'r') as f:
    scrubbed = []
    for line in f:
      scrubbed.append(line.strip())
    #print(scrubbed)
    return scrubbed

def find_row(ticket):
  #use binary to find value between 0-127 (2^7)
    exp = 0
    row = 0
    for letter in ticket[:7]:
      if letter == 'B':
        row += 2 ** (6 - exp)
      exp += 1
      if exp == len(ticket) - 1:
        exp = 0
    
    return row

def find_seat(ticket):
  #use binary to find value between 0-7 (2^3)
    exp = 0
    seat = 0
    for letter in ticket[-3:]:
      if letter == 'R':
        seat += 2 ** (2 - exp)
      exp += 1
      if exp == len(ticket) - 1:
        exp = 0
    
    return seat
    
'''def find_high_id(tickets):
#get seat/row and seat ID
  high_ticket = 0
  for ticket in tickets:
    row = find_row(ticket)
    seat = find_seat(ticket)
    ticket_id = row * 8 + seat
    print(f'row = {row}, seat = {seat}, ticket_id = {ticket_id}')
    #x = input()
    
    if ticket_id > high_ticket:
      high_ticket = ticket_id
  
  print(f'the high ticket is {high_ticket}')'''
  


#find_high_id(open_file())

def find_my_seat(tickets):
  tuples = []
  for ticket in tickets:
    row = find_row(ticket)
    seat = find_seat(ticket)
    ticket_id = row * 8 + seat
    #print(f'row = {row}, seat = {seat}, ticket_id = {ticket_id}')
    #x = input()
    
    
    tuples.append(tuple([row, seat, ticket_id]))
    
    
  seat_ids = [i[2] for i in tuples]
  #print(seat_ids)
  #
  for number in seat_ids:
    #find all id's missing neighbors
    if number + 1 not in seat_ids or number - 1 not in seat_ids:
        print(f'you probably have a neighbor at {number}')
    #whichever one is between the results is the answer, but coding 
    #that would be a bother. 
    
find_my_seat(open_file())