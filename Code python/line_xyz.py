import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_line_3d(x_range):
    """
    Hàm vẽ đường thẳng trong không gian 3D với z = -300, y = 0.

    Parameters:
    - x_range: Phạm vi giá trị x.

    Returns:
    - None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Tạo các điểm trên đường thẳng với z = -300, y = 0
    x_points = np.linspace(x_range[0], x_range[1], 100)
    y_points = np.zeros_like(x_points)
    z_points = np.full_like(x_points, -300)

    ax.plot(x_points, y_points, z_points, label='Đường thẳng')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.legend()

    plt.show()

# Vẽ đường thẳng với -100 <= x <= 100
plot_line_3d((-100, 100))
