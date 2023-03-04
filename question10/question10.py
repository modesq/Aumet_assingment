# Write a program to find the Largest sum contiguous subarray
def max_subarray_sum(arr):
    """
    Finds the maximum sum of a contiguous subarray in the given array.
    Time complexity: O(n), using Kadane's algorithm
    """
    # Initialize variables for current sum and maximum sum
    current_sum = max_sum = arr[0]
    # Loop through the array, starting at index 1
    for num in arr[1:]:
        # Calculate the current sum as the maximum of the current number and the current sum plus the number
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
    return max_sum
