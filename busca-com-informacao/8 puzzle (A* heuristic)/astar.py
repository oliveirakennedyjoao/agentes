from state import State
from board import get_possible_movements, get_frontier_nodes, is_solvable


def astar_search(inintialState: State, goalState: list):
    print("\nRunning A* search...")

    print("\nVerifing if the puzzle is solvable...")

    if (not is_solvable(inintialState.state)):
        print("\nPuzzle not solvable!\n")
        return
    else:
        print("\nPuzzle is solvable\n")

    epoch = 0
    fronteira = [inintialState]  # Lista de estados na fronteira
    visitedStates = []  # Lista de estados visitados

    print("\nInitial state: \n", inintialState)

    while fronteira:
        epoch += 1
        print("\nEpoch: ", epoch)
        print("\nFronteira: \n")

        currentNode = fronteira.pop(
            fronteira.index(min(fronteira, key=lambda state: state.cost)))

        print("Current State:", currentNode.state)

        # Verifica se o nó atual é o nó meta
        if currentNode.state == goalState:
            print("\nGoal state found!\n")
            print(currentNode)
            print("\nPath: \n")
            print(currentNode.print_path())
            break

        # Gera os estados vizinhos, ou seja, os possíveis a partir do estado atual
        frontierNodes = get_frontier_nodes(
            currentNode, goalState, get_possible_movements(currentNode.state))

        for node in frontierNodes:
            if node not in visitedStates:
                if node not in fronteira:
                    fronteira.append(node)

        fronteira.sort(key=lambda state: state.cost)
        visitedStates.append(currentNode)

        for node in fronteira:
            print(node.state, "\t cost: ", node.cost)
