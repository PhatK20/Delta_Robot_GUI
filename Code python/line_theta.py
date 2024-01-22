import DeltaKinematic_v3 as delta
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Pz = -400
Py = 0
Px_start = -50
Px_stop = 50
step = 1

for Px in np.arange(Px_start, Px_stop, step):
	P = delta.Inverse_Kinematic(Px, Py, Pz)
	if P[0]:
		print(P[1], P[2], P[3])
