__version__ = "0.7.0"

import math

def forward(l1, l2, t1, t2):
    x = l1 * math.cos(t1) + l2 * math.cos(t1 + t2)
    y = l1 * math.sin(t1) + l2 * math.sin(t1 + t2)
    return x, y

def inverse(l1, l2, x, y, elbow_up=True):
    d = (x * x + y * y - l1 * l1 - l2 * l2) / (2 * l1 * l2)
    if abs(d) > 1:
        raise ValueError("target out of reach")
    t2 = math.acos(d)
    if not elbow_up:
        t2 = -t2
    t1 = math.atan2(y, x) - math.atan2(l2 * math.sin(t2), l1 + l2 * math.cos(t2))
    return t1, t2

def jacobian(l1, l2, t1, t2):
    j11 = -l1 * math.sin(t1) - l2 * math.sin(t1 + t2)
    j12 = -l2 * math.sin(t1 + t2)
    j21 = l1 * math.cos(t1) + l2 * math.cos(t1 + t2)
    j22 = l2 * math.cos(t1 + t2)
    return [[j11, j12], [j21, j22]]

def dh_transform(a, alpha, d, theta):
    ct, st = math.cos(theta), math.sin(theta)
    ca, sa = math.cos(alpha), math.sin(alpha)
    return [
        [ct, -st * ca, st * sa, a * ct],
        [st, ct * ca, -ct * sa, a * st],
        [0, sa, ca, d],
        [0, 0, 0, 1],
    ]
