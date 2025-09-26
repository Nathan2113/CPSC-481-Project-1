from search import *


class MissCannibalsVariant(Problem):
    """ The problem of Missionaries and Cannibals.
    N1 and N2 are the total number of missionaries and cannibals starting from the left bank.
    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of missionaries on the right bank is N1-m)
    state[1] is the number of cannibals on the left bank (note: the number of cannibals on the right bank is N2-c)
    state[2] is true if boat is at the left bank, false if at the right bank """

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
        state = initial

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

        m = action.count("M")
        c = action.count("C")

        if (state[2] == True):
            state_next = (state[0] - m, state[1] - c, False)
            return state_next
        else:
            state_next = (state[0] + m, state[1] + c, True)
            return state_next

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        actions = []
        for i in range(4):
            for j in range(4 - i):
                if (i == 0 and j == 0):
                    continue

                action = ""
                for k in range(i):
                    action += "M"
                for k in range(j):
                    action += "C"

                m, c = self.result(state, action)[:2]
                m0, c0 = self.initial[:2]
                m_right = m0 - m
                c_right = c0 - c

                if (m < 0 or c < 0):
                    continue
                if (m > 0 and m < c):
                    continue
                if (m_right < 0) or (c_right < 0):
                    continue
                if (m_right > 0 and m_right < c_right):
                    continue

                actions.append(action)
        return actions


if __name__ == '__main__':
    mc = MissCannibalsVariant(4, 4)
    # Test your code as you develop! This should return  ['MC', 'MMM']
    print(mc.actions((3, 3, True)))
    print(mc.actions((2, 2, True)))

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
