from lib.Aestrela import Aestrela
from lib.ParisMetroMap import ParisMetroMap

pathFinder = Aestrela()
result = pathFinder.findPath('E7', 'E8')
# print(result.father.ID)
# print(result)

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