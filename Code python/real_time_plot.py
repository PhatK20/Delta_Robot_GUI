import sys
import numpy as np
import pyqtgraph as pg
import time  # Add this line
from pyqtgraph.Qt import QtCore, QtGui

class RealTimePlotter:
    def __init__(self):
        self.app = pg.mkQApp()

        # Set the background color of the plot
        pg.setConfigOption('background', 'w')

        self.win = pg.plot(title="Real-Time Plot")

        # Set the color of the curve
        self.curve = self.win.plot(pen={'color': 'k', 'width': 2})  # Màu đường curve là màu đen

        self.data_y = np.array([])

        # Create an array of elapsed times for the x-axis
        self.elapsed_times = np.array([])

        self.start_time = time.time()  # Record the start time

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Cập nhật mỗi giây

        # Customize the x-axis to display elapsed time
        self.win.setLabel('bottom', 'Elapsed Time', units='s')

    def update_plot(self):
        # Tạo dữ liệu giả mạo
        new_x = time.time() - self.start_time  # Thời gian đã chạy được
        new_y = np.random.rand()  # Dữ liệu giả mạo

        # Thêm dữ liệu mới vào mảng
        self.data_y = np.append(self.data_y, new_y)

        # Thêm thời gian đã chạy mới vào mảng
        self.elapsed_times = np.append(self.elapsed_times, new_x)

        # Hiển thị một số điểm trên đồ thị (có thể thay đổi tùy ý)
        max_points = 100
        if len(self.data_y) > max_points:
            self.data_y = self.data_y[-max_points:]
            self.elapsed_times = self.elapsed_times[-max_points:]

        # Cập nhật đồ thị
        self.curve.setData(self.elapsed_times, self.data_y)

if __name__ == '__main__':
    plotter = RealTimePlotter()
    sys.exit(plotter.app.exec())
