def count_messy_trios(heights):
    n = len(heights)
    messy_trios = 0

    for i in range(n):
        for j in range(i + 1, n):
            if heights[i] >= 2 * heights[j]:
                messy_trios += sum(1 for k in range(j + 1, n) if heights[j] >= 2 * heights[k])

    return messy_trios

# Example usage:
heights = [4, 5, 2, 1, 3]
print(count_messy_trios(heights))  # Output: 2

