from state import State
from astar import astar_search
from board import is_solvable

initial = State([1, 8, 2, 0, 4, 3, 7, 6, 5])
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
stateToTest = State([1, 2, 3, 4, 5, 6, 7, 0, 8])
notSolvableState = State([8, 1, 2, 0, 4, 3, 7, 6, 5])

astar_search(initial, goal)
