def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"

# Test cases
print(odd_or_even([0]))              # Output: "even"
print(odd_or_even([0, 1, 4]))        # Output: "odd"
print(odd_or_even([0, -1, -5]))      # Output: "even"
