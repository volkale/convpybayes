from datetime import date
from src.lib.prepare_input import get_stan_input


def test_get_stan_input(df_raw):

    end_date = date(2021, 12, 21)
    res_dict = get_stan_input(df_raw, end_date)

    assert res_dict['N_obs'] == 4
    assert res_dict['N_cens'] == 4
    assert (res_dict['W_obs'] == [2, 1, 2, 1]).all()
    assert (res_dict['W_cens'] == [1, 2, 1, 1]).all()
    assert (res_dict['conv_lag_obs'] == [0, 3, 0, 2]).all()
    assert (res_dict['elapsed_time'] == [4, 3, 2, 1]).all()
