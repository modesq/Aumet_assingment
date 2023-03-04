from question09 import same_elements


def test_same_elements_with_same_arrays():
    assert same_elements([1, 2, 3], [1, 2, 3]) == True
    assert same_elements([4, 5, 6], [4, 5, 6]) == True
    assert same_elements(["a", "b", "c"], ["a", "b", "c"]) == True


def test_same_elements_with_different_arrays():
    assert same_elements([1, 2, 3], [3, 2, 1]) == True
    assert same_elements([4, 5, 6], [6, 5, 4]) == True
    assert same_elements(["a", "b", "c"], ["c", "b", "a"]) == True


def test_same_elements_with_different_sizes():
    assert same_elements([1, 2, 3], [1, 2, 3, 4]) == False
    assert same_elements([4, 5, 6], [4, 5]) == False
    assert same_elements(["a", "b", "c"], ["a", "b", "c", "d"]) == False


def test_same_elements_with_different_types():
    assert same_elements([1, 2, 3], ["1", "2", "3"]) == False
    assert same_elements(["a", "b", "c"], [1, 2, 3]) == False
