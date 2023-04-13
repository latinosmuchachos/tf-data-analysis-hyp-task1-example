import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest


chat_id = 649103283 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z_stat = (p1 - p2) / np.sqrt(p * (1 - p) * ((1 / x_cnt) + (1 / y_cnt)))
    p_value = stats.norm.sf(abs(z_stat)) * 2
    return p_value < 0.03
