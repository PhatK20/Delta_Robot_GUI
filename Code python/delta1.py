import DeltaKinematic_v1 as delta
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Pool

def calculate_forward_kinematics(theta_values):
    P = delta.Forward_Kinematic(theta_values[0], theta_values[1], theta_values[2])
    if P[0]:
        return P[1], P[2], P[3]
    else:
        return None

if __name__ == '__main__':
    theta1_values = np.arange(math.radians(0), math.radians(-90), -0.5)
    theta2_values = np.arange(math.radians(0), math.radians(-90), -0.5)
    theta3_values = np.arange(math.radians(0), math.radians(-90), -0.5)

    theta_values = [(theta1, theta2, theta3) for theta1 in theta1_values
                                            for theta2 in theta2_values
                                            for theta3 in theta3_values]

    with Pool(processes=4) as pool:  # Điều chỉnh số lõi tùy ý
        results = pool.map(calculate_forward_kinematics, theta_values)

    entry = np.array([result for result in results if result is not None]).T

    # Vẽ đồ thị 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(entry[0, :], entry[1, :], entry[2, :], c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
