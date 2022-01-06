functions{
    real uncensored_lpmf(int y, real pi, real p, real lambda){
        if (y == 0) 
            return log(p) + log(pi + (1 - pi) * lambda);
        else
            return log(p) + log(1 - pi) + log(lambda) + y * log(1 - lambda);
        }

    real censoredccdf(real y, real pi, real p, real lambda){
        return log(1 - p + p * (1 - pi) * pow(1 - lambda, y + 1));
        }
        
     real invcdf(real u, real pi, real p, real lambda){
         if (u > p)
             return -1;
         else
             return ceil(log( (p - u) / (p * (1 - pi)) ) / log(1 - lambda) - 1);
     }
    
     real uncensored_rng(real pi, real p, real lambda) {
         real u;
         u = uniform_rng(0, 1);
         return invcdf(u, pi, p, lambda);
     }
}
data {
    int<lower=0, upper=1> run_estimation;
    int<lower=0> N_obs;
    int<lower=0> N_cens;
    int<lower=0> W_obs[N_obs];
    int<lower=0> W_cens[N_cens];
    int<lower=0> conv_lag_obs[N_obs];
    int<lower=0> elapsed_time[N_cens];
}
transformed data {
    int<lower = 0> N = N_obs + N_cens;
}
parameters {
    real<lower=0, upper=1> p;
    real<lower=0, upper=1> pi;
    real<lower=0, upper=1> lambda;
}
model {
    p ~ beta(2, 38);  // mean 5% P(p > 11.6%) < 5%
    pi ~ beta(1, 2);
    lambda ~ uniform(0, 1);
  
    if (run_estimation == 1) {
        for (i in 1:N_obs) {
            target += W_obs[i] * uncensored_lpmf(conv_lag_obs[i] | pi, p, lambda);
        }
        for (i in 1:N_cens) {
            target += W_cens[i] * censoredccdf(elapsed_time[i], pi, p, lambda); 
        }
    }
}
generated quantities {
    real conv_lag_pred = uncensored_rng(pi, p, lambda);
}
