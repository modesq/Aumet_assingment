# Write a program that checks if two arrays contain the same elements.
def same_elements(arr1, arr2):
    """
    Checks if two arrays contain the same elements.
    Time complexity: O(n log n) or O(n^2), depending on the sorting algorithm used
    """
    arr1.sort()
    arr2.sort()
    return arr1 == arr2
