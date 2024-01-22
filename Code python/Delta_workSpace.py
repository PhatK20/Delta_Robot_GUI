import DeltaKinematic_v3 as delta
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

entry = np.empty((3, 0))
theta1_start = 0
theta1_stop = 90
theta2_start = 0
theta2_stop = 90
theta3_start = 0
theta3_stop = 90
step = 5

for theta1 in np.arange(theta1_start, theta1_stop, step):
	for theta2 in np.arange(theta2_start, theta2_stop, step):
		for theta3 in np.arange(theta3_start, theta3_stop, step):
			P = delta.Forward_Kinematic(theta1, theta2, theta3)
			if P[0]:
				entry = np.column_stack((entry, np.array([P[1], P[2], P[3]])))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Hướng nhìn từ trục X xuống
ax.view_init(elev=0, azim=0)
ax.scatter(entry[0, :], entry[1, :], entry[2, :], c='r', marker='*')
ax.set_xticks([])        # Ẩn các giá trị trục Z
ax.set_xticklabels([])   # Ẩn nhãn trục Z
# Tự động điều chỉnh khung hiển thị
ax.auto_scale_xyz(entry[0, 1:], entry[1, 1:], entry[2, 1:])

# ax.set_xlim(0, 10)  # Đặt giới hạn trục x từ 0 đến 10
# ax.set_ylim(0, 10)  # Đặt giới hạn trục y từ 0 đến 10
# ax.set_zlim(-400, -300)  # Đặt giới hạn trục z từ 0 đến 10
ax.set_box_aspect([1, 1, 1])  # Đặt tỷ lệ chiều dài, rộng và cao của không gian
# Điều chỉnh biên để loại bỏ khoảng trắng thừa
plt.tight_layout()

# ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')

plt.show()