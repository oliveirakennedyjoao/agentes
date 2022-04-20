
from lib.BuscaGulosa import BuscaGulosa
pathFinder = BuscaGulosa()
result = pathFinder.findPath('E7', 'E8')

reducer = result
pathStack = []

while reducer:
    pathStack.append(reducer.ID)
    
    if reducer.father:
        reducer = reducer.father
    else:
        reducer = None

pathStack.reverse()
print(pathStack)