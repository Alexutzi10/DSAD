import numpy as np

def nan_replace(x):
    is_nan = np.isnan(x)
    k = np.where(is_nan)
    x[k] = np.nanmean(x[:,k[1]], axis=0)