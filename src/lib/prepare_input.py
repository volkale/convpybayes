from datetime import date
import pandas as pd


def get_stan_input(
        df: pd.DataFrame,
        end_date: date,
        visit_date_col_name='visit_date', conversion_date_col_name='conversion_date') -> dict:

    tmp = df.copy()
    tmp['frequency'] = 1
    tmp = tmp.fillna('').groupby([visit_date_col_name, conversion_date_col_name]).agg({'frequency': sum}).reset_index()
    tmp.loc[tmp[conversion_date_col_name] == '', conversion_date_col_name] = None

    cens_condition = tmp.conversion_date.isnull()
    obs_condition = tmp.conversion_date.notnull()

    N_cens = cens_condition.astype(int).sum()
    N_obs = obs_condition.astype(int).sum()

    return dict(
        run_estimation=1,
        N_obs=N_obs,
        N_cens=N_cens,
        W_obs=tmp[obs_condition].frequency.values,
        W_cens=tmp[cens_condition].frequency.values,
        conv_lag_obs=(tmp[obs_condition][conversion_date_col_name] - tmp[obs_condition][visit_date_col_name]).dt.days,
        elapsed_time=(end_date - tmp[cens_condition][visit_date_col_name]).dt.days
    )
