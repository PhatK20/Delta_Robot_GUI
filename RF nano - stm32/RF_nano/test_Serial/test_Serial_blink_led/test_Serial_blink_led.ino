#include <SPI.h>
#include <Wire.h>
#include "RF24.h"

RF24 radio(9, 10);  // Chân CE, CSN
#define LED_PIN 2
char data24bytes[] = "+0000a+0000b+0000c+0000d";

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openWritingPipe(0xF0F0F0F066LL);  // Địa chỉ truyền của RF Nano
  pinMode(LED_PIN, OUTPUT);
}

// Hàm so sánh chuỗi
bool compareStrings(const char *str1, const char *str2) {
  return strcmp(str1, str2) == 0;
}

void loop() {
  // Kiểm tra xem có dữ liệu đến từ Serial không
  if (Serial.available()) {
    // Đọc dữ liệu từ Serial
    String data = Serial.readString();

    // Chuyển đổi chuỗi sang mảng ký tự để so sánh
    char receivedData[data.length() + 1];
    data.toCharArray(receivedData, sizeof(receivedData));

    //Gửi dữ liệu qua RF
    radio.write(receivedData, sizeof(receivedData));

    // In dữ liệu đã gửi ra Serial Monitor
    Serial.print("Đã gửi qua RF Nano: ");
    Serial.println(data);

    // So sánh chuỗi và nhấp nháy LED nếu đúng chuỗi
    if (compareStrings(receivedData, data24bytes)) {
      digitalWrite(LED_PIN, HIGH);  // Bật LED
      delay(100);                  // Đợi 1 giây
      digitalWrite(LED_PIN, LOW);   // Tắt LED                
    }
  }
}
