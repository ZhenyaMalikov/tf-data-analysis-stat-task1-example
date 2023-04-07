import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 516575251 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    mean = x.mean()
    std_err = np.std(x, ddof = 1)/np.sqrt(n)
    t_val = t.ppf(0.975, df = n - 1)
    return (2 * mean)/(t_val * std_err)**2 # Ваш ответ.
