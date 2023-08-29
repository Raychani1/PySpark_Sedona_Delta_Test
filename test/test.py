import pytest


@pytest.mark.parametrize('input, output', [[True, True], [False, False]])
def test(input, output):
    assert input == output
