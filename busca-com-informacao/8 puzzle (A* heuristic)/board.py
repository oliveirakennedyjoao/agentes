# Estado inicial
from state import State


def count_inversions(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions


def is_solvable(state):
    inversions = count_inversions(state)
    if len(state) % 2 == 1:
        return inversions % 2 == 0
    else:
        blank_row = state.index(0) // 3
        return (blank_row % 2 == 0 and inversions % 2 == 0) or (blank_row % 2 == 1 and inversions % 2 == 1)


# Get the index of the value in the state or position of 0 if value is passed


def find_blank_position(state: list):
    return state.index(0)

# Get the number of misplaced numbers h1(n)


def misplacedNumbers(state, goal_state):
    misplaced = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            misplaced += 1
    return misplaced

# Get the number of movements to the number reach its correct position h2(n)
# It uses the manhattan distance to calculate the distance of each number to its goal position


def distanceToGoal(state: list, goal_state: list):
    distance = 0
    n = int(len(state) ** 0.5)
    for i in range(len(state)):
        current_value = state[i]
        goal_index = goal_state.index(current_value)
        current_coords = (i // n, i % n)
        goal_coords = (goal_index // n, goal_index % n)
        d = abs(current_coords[0] - goal_coords[0]) + \
            abs(current_coords[1] - goal_coords[1])
        distance += d
        # print("distance of: ", current_value, " is -> ", d)
    return distance


def get_possible_movements(state):
    blank_position = find_blank_position(state)
    i = blank_position // 3
    j = blank_position % 3
    neighbors_positions = []
    if i > 0:
        neighbors_positions.append((blank_position - 3, "MOVER_PARA_CIMA"))
    if i < 2:
        neighbors_positions.append((blank_position + 3, "MOVER_PARA_BAIXO"))
    if j > 0:
        neighbors_positions.append((blank_position - 1, "MOVER_PARA_ESQUERDA"))
    if j < 2:
        neighbors_positions.append((blank_position + 1, "MOVER_PARA_DIREITA"))
    return neighbors_positions

# give me a function that change the position of thwo elements in the state


def change_position(state: list, blank_position: int, new_blank_position: int):
    new_state = state.copy()
    new_state[blank_position], new_state[new_blank_position] = new_state[new_blank_position], new_state[blank_position]
    return new_state

# Gera os estados vizinhos, ou seja, os possíveis a partir do estado atual


def get_frontier_nodes(state: State, goal_state: list, possible_movements: list) -> State:
    blank_position = find_blank_position(state.state)
    neighbors_states = []
    for blank_possible_position in possible_movements:
        new_state = change_position(
            state.state, blank_position, blank_possible_position[0])
        neighbors_states.append(
            State(new_state, state, blank_possible_position[1], state.cost, distanceToGoal(new_state, goal_state)))
    return neighbors_states
