# -*- coding: utf-8 -*-

def list_divide(numbers, divide = 2):
    """
    The function returns the number of elements in the numbers list that are divisible by divide
    """
    numcount = 0
    for x in numbers:
        if x % divide == 0:
            numcount += 1
    return numcount

#class that raises exception
class ListDivideException(Exception):
    pass


def test_list_divide():
    """
    Test list_divide
    """
   
    try:
       
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide = 10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
       
    except AssertionError:
        raise ListDivideException
       
if __name__ == "__main__":
   
    test_list_divide()

