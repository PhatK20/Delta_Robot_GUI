import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
import cv2

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.video_label = QLabel(self.central_widget)
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_button = QPushButton("Start Camera", self.central_widget)
        self.stop_button = QPushButton("Stop Camera", self.central_widget)
        self.stop_button.setEnabled(False)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.camera = cv2.VideoCapture(0)  # 0 là chỉ số của camera (có thể thay đổi)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.start_button.clicked.connect(self.start_camera)
        self.stop_button.clicked.connect(self.stop_camera)

    def start_camera(self):
        if not self.timer.isActive():
            self.timer.start(16)  # 16 ms là khoảng thời gian giữa các khung hình
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    def stop_camera(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = image.shape
            bytes_per_line = ch * w
            convert_to_qt_format = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(convert_to_qt_format)
            self.video_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec())
