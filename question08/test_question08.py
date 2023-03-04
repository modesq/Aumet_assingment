from question08 import is_prime


def test_is_prime_with_prime_number():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(19) == True


def test_is_prime_with_non_prime_number():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(21) == False
    assert is_prime(27) == False


def test_is_prime_with_zero_and_one():
    assert is_prime(0) == False
    assert is_prime(1) == False


def test_is_prime_given_examples():
    assert is_prime(49) == False
    assert is_prime(19) == True
