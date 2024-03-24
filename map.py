from setting import *

text_map = [
    'WWWWWWWWWWWWWWW',
    'W...W...W...W.W',
    'W.W....WWWW...W',
    'W....W......W.W',
    'W...W.........W',
    'W...W...WW..W.W',
    'W..W......W.W.W',
    'WWWWWWWWWWWWWWW'
]

world_map = set()
for i, row in enumerate(text_map):
    for j, elem in enumerate(row):
        if elem == 'W':
            world_map.add((j * TILE_WIDTH, i * TILE_HEIGHT))