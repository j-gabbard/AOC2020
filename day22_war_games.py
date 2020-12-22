import time
import re
import itertools
import sys

def open_file():
  #going to open file and clean up data
  with open('./inputs/day22.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    #return scrubbed
    
    deck1, deck2 = scrubbed[1:scrubbed.index('Player 2:')], scrubbed[scrubbed.index('Player 2:') +1 :]
    del deck1[-1] #need to kill the newline
    deck1 = [int(x) for x in deck1]
    deck2 = [int(x) for x in deck2]
    
    return deck1, deck2


def make_war(deck1, deck2):
  
  while deck1 and deck2:
    card1, card2 = deck1.pop(0), deck2.pop(0)
    
    if card1 > card2: 
      deck1.extend([card1, card2])
    if card1 < card2: 
      deck2.extend([card2, card1])
    
  #print(deck1, deck2)
  score = 0
  for multiplier in range(1, len(deck1) + 1):
    score += multiplier * deck1.pop(-1)
  
  return(deck1, score)
  
def calculate_score(deck):
  score = 0
  for multiplier in range(1, len(deck) + 1):
    score += multiplier * deck.pop(-1)
  
  return score

def dupe_check(deck1, deck2, p1_deck_states, p2_deck_states, game):

  if deck1 in p1_deck_states[game] and deck2 in p2_deck_states[game]:
    return True
  else: 
    return False
    

hand_counter = 0
game_counter = 0
def game2(deck1, deck2, game):
  global hand_counter
  global game_counter
  global p1_deck_states
  global p2_deck_states
  p1_deck_states[game], p2_deck_states[game] = [], []
  flag = False
  
  while deck1 and deck2 and not flag:
    card1, card2 = deck1.pop(0), deck2.pop(0)
    
    if dupe_check(deck1, deck2, p1_deck_states, p2_deck_states, game):
      #hold_up = input()
      game_winner = 1
      flag = True
      break
    
    p1_deck_states[game].append(deck1[:])
    p2_deck_states[game].append(deck2[:])
    
    if card1 <= len(deck1) and card2 <= len(deck2):
      hand_winner = game2(deck1[:card1], deck2[:card2], game + 1)
      #print(card1, card2)
      #hold_up = input()
        
    elif card1 > card2:
      hand_winner = 1
    elif card2 > card1:
      hand_winner = 2

    #process winner, put cards on bottom, update dict  
    if hand_winner == 1:
      deck1.extend([card1, card2])
    if hand_winner == 2:
      deck2.extend([card2, card1])

    hand_counter += 1
    if hand_counter % 1000 == 0:
      print(f'hands: {hand_counter}')

  #this could probably be "if deck1" and "if deck2" but don't want to troubleshoot:
  if len(deck1) > len(deck2) and not flag:
    game_winner = 1
  elif len(deck1) < len(deck2) and not flag:
    game_winner = 2
    
  #game_counter += 1
  #print(f'games: {game_counter}')
  
  if game > 1:
    del p1_deck_states[game]
    del p2_deck_states[game]
    return game_winner
  
  if game == 1 and game_winner == 1:
    print(calculate_score(deck1))
  elif game == 1 and game_winner == 2:
    print(calculate_score(deck2))
  
  
    
 
    
    
  
  
  
  
'''
did game end because same game state?

  flip card
    did we cause iterative game?
      If yes, who won? Clean up states and return winner. 
      If no, who won this round? Put cards on bottom of deck
    
    update dict 
  
    

deck1, deck2 = open_file()'''
t = time.time()
#print(make_war(deck1, deck2))
p1_deck_states, p2_deck_states = dict(), dict()
deck1, deck2 = open_file()
game2(deck1, deck2, 1)
print(f'took {time.time()-t} seconds')