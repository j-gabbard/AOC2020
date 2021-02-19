import time
import re
import itertools
import sys

def open_file():
  #going to open file and clean up data
  with open('./inputs/day20.txt', 'r') as f:
    raw = f.read()
    #scrubbed = [x.strip() for x in f.readlines()]    
    #ordered = sorted(scrubbed)
    return raw

def generate_tiles(inp):
  tile_dict = dict()
  blocks = inp.split('\n\n')
  for x in blocks:
    idx, tile = x.split(':\n')[0][5:], x.split('\n')[1:]
    tile_dict[idx] = [a.split() for a in tile if a != '']
  
  return tile_dict

def rotate_clockwise(tile):
  #given a tile, rotate it clockwise
  output = list(zip(*original[::-1]))
  return output

def get_edges(tile):
  #get the 4 edges from a given tile
  left, right = [], [] 
  upper = ''.join(tile[0])
  lower = ''.join(tile[-1])
  for x in tile:
    left.extend(x[0][0])
    right.extend(x[0][-1])
    
  leftout = ''.join(left)
  rightout = ''.join(right)
  #print(upper, lower, leftout, rightout)
  
  
def match():
  tiles = generate_tiles(open_file())
  edges_dict = dict()
  for index, tile in tiles.items():
    print(index, tile)
    hold_on = input()
    edges_dict[index] = get_edges(tile)
  
  print(edges_dict)
  
match()
    
#temp_dict = generate_tiles(open_file())
#print(temp_dict)
get_edges(generate_tiles(open_file())['2797'])
  
  


#t = time.time()
#print(f'took {time.time()-t} seconds')