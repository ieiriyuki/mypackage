import pandas as pd
from pandas import testing
import pytest

from package2.bar.bar import bar

@pytest.mark.parametrize(
    "a",
    [1],
)
def test_bar(a):
    assert a == 1
    testing.assert_series_equal(bar(), pd.Series(["bar"]))
