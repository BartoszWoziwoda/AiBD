from my_function import bubblesort

import pytest

testdata = [
    ([1,3,2,64,12,5],[1,2,3,5,12,64]),
    ([79453,42314,654,324,76,2,6],[2,6,76,324,654,42314,79453])
    ]

@pytest.mark.parametrize('lst, expected_lst', testdata)
def test_bubblesort(lst, expected_lst):

    assert bubblesort(lst) == expected_lst