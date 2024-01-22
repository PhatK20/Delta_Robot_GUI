import cv2
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QTimer

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.cap = cv2.VideoCapture(0)

        self.central_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.start_button = QtWidgets.QPushButton("Start Camera")
        self.start_button.clicked.connect(self.start_camera)
        self.layout.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton("Stop Camera")
        self.stop_button.clicked.connect(self.stop_camera)
        self.layout.addWidget(self.stop_button)

        self.image_label = QtWidgets.QLabel()
        self.layout.addWidget(self.image_label)

    def start_camera(self):
        self.timer.start(20)

    def stop_camera(self):
        self.timer.stop()

    def update_frame(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format.Format_RGB888)
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
