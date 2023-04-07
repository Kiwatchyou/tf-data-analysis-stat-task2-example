import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 390760498 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t = 35
    alpha = 1 - p
    min = (-x).min()
    z = -np.log(1-p)/x.size    
    return 2*(-min-1/2)/(t*t), 2*(z-min-1/2)/(t*t)

