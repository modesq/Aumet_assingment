from question10 import max_subarray_sum


def test_max_subarray_sum_all_positive():
    arr = [1, 2, 3, 4, 5]
    expected = 15
    assert max_subarray_sum(arr) == expected


def test_max_subarray_sum_all_negative():
    arr = [-1, -2, -3, -4, -5]
    expected = -1
    assert max_subarray_sum(arr) == expected


def test_max_subarray_sum_mixed():
    # which is the given example too
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    assert max_subarray_sum(arr) == expected


def test_max_subarray_sum_one_element():
    arr = [5]
    expected = 5
    assert max_subarray_sum(arr) == expected
