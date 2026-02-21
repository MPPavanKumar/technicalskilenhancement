class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, arr)

    # Build segment tree
    def _build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2

            self._build(left, start, mid, arr)
            self._build(right, mid + 1, end, arr)

            self.tree[node] = max(self.tree[left], self.tree[right])

    # Update index with value
    def update(self, idx, value):
        self._update(0, 0, self.n - 1, idx, value)

    def _update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2

            if idx <= mid:
                self._update(left, start, mid, idx, value)
            else:
                self._update(right, mid + 1, end, idx, value)

            self.tree[node] = max(self.tree[left], self.tree[right])

    # Query maximum in range [L, R]
    def queryMax(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        # Completely outside
        if R < start or end < L:
            return float("-inf")

        # Completely inside
        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        leftMax = self._query(2 * node + 1, start, mid, L, R)
        rightMax = self._query(2 * node + 2, mid + 1, end, L, R)

        return max(leftMax, rightMax)


# ---------------- Example ----------------

if __name__ == "__main__":
    prices = [100, 80, 120, 90, 150, 70]

    st = SegmentTree(prices)

    print("Max [1,4]:", st.queryMax(1, 4))  # 150

    st.update(3, 200)  # update index 3

    print("Max [1,4] after update:", st.queryMax(1, 4))  # 200