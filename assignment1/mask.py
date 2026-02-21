def min_cost_assignment(cost):
    n = len(cost)
    size = 1 << n  # 2^n

    # Initialize DP array
    dp = [float('inf')] * size
    dp[0] = 0  # base case: no workers assigned

    for mask in range(size):
        # Count assigned tasks = number of set bits
        task = bin(mask).count("1")

        if task >= n:
            continue

        for worker in range(n):
            # If worker not assigned yet
            if not (mask & (1 << worker)):
                new_mask = mask | (1 << worker)
                dp[new_mask] = min(
                    dp[new_mask],
                    dp[mask] + cost[task][worker]
                )

    return dp[size - 1]


# ---------------- Example ----------------

if __name__ == "__main__":
    cost_matrix = [
        [9, 2, 7],
        [6, 4, 3],
        [5, 8, 1]
    ]

    print("Minimum Assignment Cost:",
          min_cost_assignment(cost_matrix))