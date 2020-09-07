

class KnapSack(object):
    """Implements the KnapSack algorithm and stores data for GUI to make use of."""

    def __init__(self, items=[], size=0):
        super(KnapSack, self).__init__()
        self.items = items
        self.size = size
        self.dp = []

    def solve(self):
        # Stores solution table in self.dp

        # Initialize a mxn table where m=self.size and n=len(self.items)
        dp = [[0 for i in range(len(self.items)+1)]
              for s in range(self.size+1)]

        for i in range(1, len(self.items)+1):
            for s in range(self.size+1):
                taken, not_taken = 0, dp[s][i-1]
                # self.items is 0-indexed as usual, but in self.dp 0 means 0 items. (dp[i] <-> items[i-1])
                if s >= self.items[i-1].weight:
                    taken = self.items[i-1].value + dp[s-self.items[i-1].weight][i-1]
                dp[s][i] = max(taken, not_taken)
        self.dp = dp
        return dp

    def _build_from_lists(self, weights, values, size):
        for w, v in zip(weights, values):
            self.items.append(KSItem(w, v))
        self.size = size


class KSItem(object):
    
    def __init__(self, weight, value, img_filename=None):
        self.weight = weight
        self.value = value
        self.img_filename = img_filename
