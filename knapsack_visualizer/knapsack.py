

class KnapSack(object):
    """Implements the KnapSack algorithm and stores data for GUI to make use of."""

    def __init__(self, items=[], size=0):
        super(KnapSack, self).__init__()
        self.items = items
        self.size = size
        self.dp = []

    def solve(self):
        # Stores solution table in self.dp
        if not (self.items[0].weight == 0 and self.items[0].value == 0):
            self.items = [KSItem(0, 0)] + self.items # Make self.items start at 1 (0 stands for no items)

        # Initialize a mxn table where m=self.size and n=len(self.items)
        dp = [[0 for i in range(len(self.items))]
              for s in range(self.size+1)]

        for i in range(1, len(self.items)):
            for s in range(self.size+1):
                taken, not_taken = 0, dp[s][i-1]
                # self.items is 0-indexed as usual, but in self.dp 0 means 0 items. (dp[i] <-> items[i-1])
                if s >= self.items[i].weight:
                    taken = self.items[i].value + dp[s-self.items[i].weight][i-1]
                dp[s][i] = max(taken, not_taken)
        self.dp = dp
        return dp

    def _build_from_lists(self, weights, values, size, filenames=None):
        self.items = []
        if not filenames: filenames = [None] * len(weights)
        for w, v, f in zip(weights, values, filenames):
            self.items.append(KSItem(w, v, f))
        self.size = size
    
    def _verify_items(self):
        item_0 = self.items[0]; item_1 = self.items[1]
        # Checking that item 0 is dummy and item 1 is not
        if (item_0.weight == 0 and item_0.value == 0) and (item_1.weight != 0):
            return 0
        raise ValueError

    def dp_parents(self, row, col):
        if row>= self.items[col].weight:
            return (row, col-1), (row-self.items[col].weight, col-1), 
        return (row, col-1)


class KSItem(object):

    def __init__(self, weight, value, filename=None):
        self.weight = weight
        self.value = value
        self.filename = filename

if __name__ == '__main__':
    ks = KnapSack()
    ks._build_from_lists([1,2,3], [6,10,12], 5)
    ks.solve()
    TMP = ks.dp
    print(TMP)
