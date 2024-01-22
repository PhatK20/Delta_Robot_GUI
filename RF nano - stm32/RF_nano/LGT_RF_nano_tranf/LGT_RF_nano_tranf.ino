#include <SPI.h>
#include <Wire.h>
#include "RF24.h"

RF24 radio(9, 10);  // Chân CE, CSN

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openWritingPipe(0xF0F0F0F0E1LL);  // Địa chỉ truyền của RF Nano
}

void loop() {
  // Kiểm tra xem có dữ liệu đến từ Serial không
  if (Serial.available()) {
    // Đọc dữ liệu từ Serial
    String data = Serial.readString();

    // Chuyển đổi chuỗi sang mảng ký tự 
    char receivedData[data.length() + 1];
    data.toCharArray(receivedData, sizeof(receivedData));

    //Gửi dữ liệu qua RF
    radio.write(receivedData, sizeof(receivedData));
  }
}
