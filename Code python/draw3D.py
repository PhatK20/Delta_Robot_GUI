import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo một đối tượng hình 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dữ liệu
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [1, 2, 3, 4, 5]

# Vẽ đồ thị 3D
ax.scatter(x, y, z, c='r', marker='o')

# Thiết lập nhãn
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
