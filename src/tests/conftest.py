import pytest
import pandas as pd
from datetime import date


@pytest.fixture
def df_raw():
    data = [
        [date(2021, 12, 17), date(2021, 12, 17)],
        [date(2021, 12, 17), date(2021, 12, 17)],
        [date(2021, 12, 17), date(2021, 12, 20)],
        [date(2021, 12, 17), None],
        [date(2021, 12, 18), date(2021, 12, 18)],
        [date(2021, 12, 18), date(2021, 12, 18)],
        [date(2021, 12, 18), date(2021, 12, 20)],
        [date(2021, 12, 18), None],
        [date(2021, 12, 18), None],
        [date(2021, 12, 19), None],
        [date(2021, 12, 20), None]
    ]
    return pd.DataFrame(data, columns=['visit_date', 'conversion_date'])
