from collections import deque
from src.settings import *

# Define a bfs search for the following direcitons to get to the given point
def bfs(foodx, foody):
    d = deque()
    directions = [[SNAKE_BLOCK, 0], [-SNAKE_BLOCK, 0], [SNAKE_BLOCK, ]]