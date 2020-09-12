

class KnapSack(object):
    """Implements the KnapSack algorithm and stores data for GUI to make use of."""

    def __init__(self, items=[], size=0):
        super(KnapSack, self).__init__()
        self.items = items
        self.size = size
        self.dp = []
        self.pars = {}

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
                if s >= self.items[i].weight:
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
    
    def dp_parents_sorted(self, row, col):
        return self.pars.get((row, col), [])


class KSItem(object):

    def __init__(self, weight, value, filename=None):
        self.weight = weight
        self.value = value
        self.filename = filename

if __name__ == '__main__':
    ks = KnapSack()
    ks._build_from_lists([1,2,3], [6,10,12], 5)
    ks.solve()
    print(ks.dp)
    print()
    print(ks.pars)
