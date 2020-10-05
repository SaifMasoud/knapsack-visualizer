import numpy as np
from pprint import pprint

class BaseDPAlgorithm:
    """Base Class for creating classes implementing dp-table algorithms. Inherit this class to make a consistent interface
     for the GUI to use. Note: It is not required to inherit this as long as get_cell_value and get_cell_parents are implemented."""
    
    def __init__(self):
        self.dp = [] # You can use an array, dictionary, or something else to represent the dp table.
        self.pars = {}
        self.gui_vert_headers = []
        self.gui_horizontal_headers = []

    def get_cell_value(self, row, col):
        raise NotImplementedError

    def get_cell_parents(self, row, col):
        """Should return row,col for all parent candidates, with the 1st one being the actual/best parent."""
        raise NotImplementedError

class LCS(BaseDPAlgorithm):
    def __init__(self, s1, s2):
        super().__init__()
        self.s1 = s1
        self.s2 = s2
        self.gui_horizontal_headers = ['-'] + list(s1)
        self.gui_vert_headers = ['-'] + list(s2)
        self.solve()

    def solve(self):
        s1, s2 = self.s1, self.s2
        dp = [[0 for col in range(len(s1)+1)] for row in range(len(s2)+1)]
        for col in range(1, len(s1)+1):
            for row in range(1, len(s2)+1):
                if s1[col-1] == s2[row-1]: # -1 becasue row/col 0 stands for no chars from the string, i.e the dp assumes 1-indexing 
                    dp[row][col] = 1 + dp[row-1][col-1]
                    self.pars[row, col] = (row-1, col-1)
                elif dp[row-1][col] > dp[row][col-1]:
                    dp[row][col] = dp[row-1][col]
                    self.pars[row, col] = (row-1, col)
                else:
                    dp[row][col] = dp[row][col-1]
                    self.pars[row, col] = (row, col-1)
        self.dp = dp
    
    def get_cell_value(self, row, col):
        return str(self.dp[row][col])

    def get_cell_parents(self, row, col):
        if row==0 or col==0:
            return [(0, 0)]
        return [self.pars[row, col]]
    
    def _lcs_path(self):
        end = (len(self.s2), len(self.s1))
        cur = end
        while self.pars.get(cur, None) is not None:
            prev = cur
            cur = self.pars[cur]
            if cur==(prev[0]-1, prev[1]-1): path.append(cur)
        print(path[::-1])
        return path[::-1]

class KnapSack(BaseDPAlgorithm):
    """Implements the KnapSack algorithm and stores data for GUI to make use of."""

    def __init__(self, weights, values, size=0):
        super().__init__()
        self.items = []
        self.build_and_solve(weights, values, size)

    def solve(self):
        # Initialize a mxn table where m=self.size and n=len(self.items)
        dp = [[0 for i in range(len(self.items))]
              for s in range(self.size+1)]
        for s in range(self.size+1):
            dp[s][0] = self.items[0].value if self.items[0].weight <= s else 0

        for i in range(1, len(self.items)):
            for s in range(self.size+1):
                taken, not_taken = 0, dp[s][i-1]
                self.pars[s, i] = [(s, i-1)]
                if s >= self.items[i].weight: # if its possible to take the item
                    taken = self.items[i].value + dp[s-self.items[i].weight][i-1]
                    temp_pars = [(s, i-1), (s-self.items[i].weight, i-1)]
                    self.pars[s, i] = temp_pars if not_taken>taken else list(reversed(temp_pars))
                dp[s][i] = max(taken, not_taken)
        self.dp = dp
        return dp

    def _build_from_lists(self, weights, values, size, filenames=None):
        self.items = []
        if not filenames: filenames = [None] * len(weights)
        for w, v, f in zip(weights, values, filenames):
            self.items.append(KSItem(w, v, f))
        self.size = size
    
    def build_and_solve(self, weights, values, size, filenames=None):
        self._build_from_lists(weights, values, size, filenames)
        self.solve()
        self.gui_horizontal_headers = [str(item.value) for item in self.items]
        self.gui_vert_headers = [str(i) for i in range(self.size+1)]
    
    def dp_parents_sorted(self, row, col):
        return self.pars.get((row, col), [])
    
    def get_cell_value(self, row, col):
        return str(self.dp[row][col])
    
    def get_cell_parents(self, row, col):
        return self.pars.get((row, col), [])

class KSlotKnapSack:
    """ Variation of knapsack where you have to do exactly k takes for s size(values are True/False if possible/not)."""
    def __init__(self, weights, size, slots):
        self.dp = []
        self.pars = {}
        self.slots = slots
        self.weights = weights
        self.size = size
        self.gui_horizontal_headers = ['0'] + [str(w) for w in self.weights]
        self.gui_vert_headers = [str(i) for i in range(size+1)]
        self.solve()
    
    def solve(self):
        self.weights = [0] + self.weights # dummy item
        # dp[s][i][k]
        dp = [[[False for k in range(self.slots+1)] for i in range(len(self.weights))] for s in range(self.size+1)]
        dp[0][0][0] = True # using 0 takes, 0 size, no items, its Possible to do so.
        for col in range(1, len(self.weights)):
            for row in range(self.size+1):
                for k in range(self.slots+1):
                    if k==0==row: # We can get a knapsack filled with 0 slots if zero size.
                        dp[row][col][k] = True
                        continue
                    not_taken, taken = dp[row][col-1][k], False
                    if row >= self.weights[col]: # if we can take
                        taken = dp[row-self.weights[col]][col-1][k-1]
                    dp[row][col][k] = max(taken, not_taken)
        self.dp = dp

    def get_cell_value(self, row, col):
        print("Getting ", (row, col))
        return str(self.dp[row][col])

class KSItem(object):
    def __init__(self, weight, value, filename=None):
        self.weight = weight
        self.value = value
        self.filename = filename

if __name__ == '__main__':
    ks = KnapSack([1,2,3], [6, 10, 12], 5)
    import numpy as np
    print(np.matrix(ks.dp))

    lcs = LCS("Hello", "Hillosoad")
    print(lcs._lcs_path())