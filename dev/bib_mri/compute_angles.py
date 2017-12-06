# -*- encoding: utf-8 -*-
import numpy as np

def compute_angles(pivot, anterior, posterior):
    max_angle = np.pi*2

    def angles(vectors):
        return np.arctan2(vectors[1], vectors[0])

    ap, pp = anterior-pivot, posterior-pivot
    ang_post, ang_ant = angles(pp), angles(ap)
    ang = ang_post - ang_ant

    dif_prof = np.abs(ang - np.roll(ang,1)) > np.pi
    ind_start = np.where(dif_prof)[0][::2]
    ind_end = np.where(dif_prof)[0][1::2]
    zeros = np.zeros_like(ang)
    for in1, in2 in zip(ind_start,ind_end):
	if (ang[in1] - np.roll(ang,1)[in1]) > np.pi:
	    zeros[in1:in2] = -2*np.pi
	else:
	    zeros[in1:in2] = 2*np.pi

    return (ang + zeros) *180/(np.pi)
