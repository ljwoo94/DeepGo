'''
Script to create zobrist hash table.
 -> Can be changed to file Io.
'''
import random
from dlgo.gotypes import Player, Point

def to_python(player_state):
    if player_state is None:
        return 'None'

    if player_state == Player.black:
        return Player.black
    return Player.white

MAX63 = 0x7fffffffffffffff

''' 
Define hash Table for zobrist hash. (Pre-defined Hash Table)
Each value in table refers the state of go board coordinates
MAX BOARD = 19,19
'''
table = {}
empty_board = 0
for row in range(1,20):
    for col in range(1,20):
        for state in (Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code

print('from dlgo.gotypes import Player, Point')
print('')
print("__all__ = ['HASH_CODE', 'EMPTY_BOARD']")
print('')
print('HASH_CODE = {')
for (pt, state), hash_code in table.items():
    print(' (%r, %s): %r, ' % (pt, to_python(state), hash_code))
print('}')
print('')
print('EMPTY_BOARD = %d' % (empty_board,))

