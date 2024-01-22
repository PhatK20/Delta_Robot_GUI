#include <RF24.h>

RF24 radio(9, 10);  // Chân CE, CSN

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openWritingPipe(0xF0F0F0F0E1LL);  // Địa chỉ truyền của RF Nano
}

void loop() {
  // Đọc dữ liệu từ Serial khi có sẵn
  if (Serial.available() >= 24) {
    char dataFromPC[24];
    Serial.readBytes(dataFromPC, 24);

    // Hiển thị dữ liệu nhận được từ Python
    Serial.print("Đã nhận từ Python: ");
    Serial.println(dataFromPC);

    // Gửi dữ liệu từ RF Nano đến Arduino Uno qua RF24
    radio.write(dataFromPC, sizeof(dataFromPC));
    Serial.print("Đã gửi qua RF Nano: ");
    Serial.println(dataFromPC);
  }

  // Thêm một đoạn mã xử lý thêm ở đây nếu cần thiết
  // ...
  
  // Đợi một khoảng thời gian trước khi kiểm tra lại
  delay(1000);
}
