class State:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = g + h  # f(n) = g(n) + h(n)
        self.g = g  # Aqui vai ser a distância percorrida do nó origem até o nó atual
        self.h = h  # Aqui vai ser a distância percorrida do nó
        # origem até o nó atual + a distância do nó atual até o nó meta

    def __str__(self):
        return """\n|  {0}  {1}  {2}  |\n|  {3}  {4}  {5}  |\n|  {6}  {7}  {8}  |\n""".format(
            self.state[0], self.state[1], self.state[2],
            self.state[3], self.state[4], self.state[5],
            self.state[6], self.state[7], self.state[8])

    def __eq__(self, other):
        return self.state == other.state

    def print_path(self):
        if self.parent:
            self.parent.print_path()
        print(
            'Estado inicial:' if not self.action and not self.parent else 'Fim.\n' if not self.action else 'Action: %s' % (self.action))
        print(self, "\n")
