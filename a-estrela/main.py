from lib.Aestrela import Aestrela

pathfinder = Aestrela()
result = pathfinder.findPath('E7', 'E8')
# print(result)

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

