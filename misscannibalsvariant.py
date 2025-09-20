from search import *

class MissCannibalsVariant(Problem):
    """ The problem of Missionaries and Cannibals. 
    N1 and N2 are the total number of missionaries and cannibals starting from the left bank.
    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of missionaries on the right bank is N1-m)
    state[1] is the number of cannibals on the left bank (note: the number of cannibals on the right bank is N2-c)
    state[2] is true if boat is at the left bank, false if at the right bank """

    action = [
            'M', 'C', 
            'MM', 'MC', 'CC',
            'MMM', 'MMC', 'MCC', 'CCC'
    ]

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
        state = initial
    
    def result(self, state, action):
        m_left, c_left, left = state

        #print(f"Missionaries: {m}")
        #print(f"Cannibals: {c}")
        #print(f"onLeft: {left}")

        #state = (m - 1, c - 1, False)

        #m, c, left = state

        #print(f"Missionaries: {m}")
        #print(f"Canniabls: {c}")
        #print(f"onLeft: {left}")




    """Returns all valid actions from the current state."""
    def actions(self, state):
        m_left, c_left, left = state

        m_available = m_left if left else (self.N1 - m_left)
        c_available = c_left if left else (self.N2 - c_left)

        valid = []
        for i in self.action:
            number_m = self.action.count('M')
            number_c = self.action.count('C')

        
            # Checking capacity and availability
            if number_m + number_c == 0 or number_m + number_c > 3:
                continue
            if number_m > m_available or number_c > c_available:
                continue

            # Move people across and compute next state
            if left:
                m_next = m_left - number_m
                c_next = c_left - number_c
        
            valid.append(i)


        return valid    


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    # print(mc.actions((3, 3, True))) # Test your code as you develop! This should return  ['MC', 'MMM']
    print(mc.result(mc.initial, None))
    print(mc.actions((3, 3, True)))

    #path = depth_first_graph_search(mc).solution()
    #print(path)
    #path = breadth_first_graph_search(mc).solution()
    #print(path)

