# -*- encoding: utf-8 -*-
import numpy as np

def compute_angles(pivot, anterior, posterior):
    max_angle = np.pi*2

    def angles(vectors):
        return np.arctan2(vectors[0], vectors[1])

    ap, pp = anterior-pivot, posterior-pivot

    ang_post, ang_ant = angles(pp), angles(ap)
    ang = ang_post - ang_ant
    idx = ang<-(3*np.pi/2.0)
    ang[idx] = (ang[idx]+(2*np.pi))
    idx = ang<0.75
    ang[idx] += max_angle
    return 360 - ang*180/(np.pi)
