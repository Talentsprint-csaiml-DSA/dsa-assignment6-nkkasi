def longest_box_sequence(boxes):
    # Step 1: Sort the dimensions of each box
    boxes = [tuple(sorted(box)) for box in boxes]
    
    # Step 2: Sort the boxes by their dimensions
    boxes.sort()

    # Step 3: Find the longest increasing subsequence based on box dimensions
    n = len(boxes)
    dp = [1] * n  # Initialize DP array to store LIS lengths

    for i in range(1, n):
        for j in range(i):
            if (boxes[j][0] < boxes[i][0] and
                boxes[j][1] < boxes[i][1] and
                boxes[j][2] < boxes[i][2]):
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the largest number of boxes that can be packed
    return max(dp)

# testing
""" boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]
result = longest_box_sequence(boxes)
print(result)  # Output: 2 """
