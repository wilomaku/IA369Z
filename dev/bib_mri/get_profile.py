# -*- encoding: utf-8 -*-
import numpy as np
import scipy.interpolate as spline
import bib_mri as FW

def get_profile(tck, n_samples, radius):
    def eval_spline(tck, t):
        y, x = spline.splev(t,tck)
        return np.vstack((y,x))
    t_pivot = np.linspace(0,1, n_samples, endpoint=False)
    pivot = eval_spline(tck, t_pivot)
    t_anterior = np.mod(t_pivot+(1-radius), 1)
    anterior = eval_spline(tck, t_anterior)
    t_posterior = np.mod(t_pivot+radius, 1)
    posterior = eval_spline(tck, t_posterior)
    return FW.compute_angles(pivot, anterior, posterior)

