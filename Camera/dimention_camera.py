import cv2

# Mở camera
cap = cv2.VideoCapture(0)  # Thay đổi số này tùy thuộc vào cổng camera của bạn

# Đọc một khung hình từ camera
ret, frame = cap.read()

# Lấy kích thước của khung hình
height, width, channels = frame.shape

print('Width: ', width)
print('Height: ', height)

# Đảm bảo rằng bạn đã giải phóng camera sau khi sử dụng
cap.release()
