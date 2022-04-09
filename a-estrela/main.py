from lib.Aestrela import Aestrela

pathfinder = Aestrela()
result = pathfinder.findPath('E10', 'E7')

path = []
node = result
while node:
    path.append(node.ID)
    
    if node.father:
        node = node.father
    else:
        node = None

path.reverse()
print(path)

