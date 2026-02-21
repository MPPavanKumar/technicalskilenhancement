from collections import deque

class StreamingMax:
    def __init__(self, k):
        self.k = k
        self.deque = deque()   # stores indices
        self.data = []
        self.i = 0

    # Process one incoming latency value (streaming)
    def push(self, value):
        self.data.append(value)

        # Remove elements smaller than current from back
        while self.deque and self.data[self.deque[-1]] <= value:
            self.deque.pop()

        # Add current index
        self.deque.append(self.i)

        # Remove out-of-window index from front
        if self.deque[0] <= self.i - self.k:
            self.deque.popleft()

        self.i += 1

        # Return max once first window is complete
        if self.i >= self.k:
            return self.data[self.deque[0]]
        return None


# ---------------- Batch Version ----------------

def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):

        # Remove smaller elements from back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Remove indices out of window
        if dq[0] <= i - k:
            dq.popleft()

        # Append max once window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ---------------- Example ----------------

if __name__ == "__main__":
    data = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(sliding_window_max(data, k))

    # Streaming example
    sm = StreamingMax(k)
    for x in data:
        m = sm.push(x)
        if m is not None:
            print(m, end=" ")