#include <RF24.h>

RF24 radio(9, 10);  // Chân CE, CSN
#define LED_PIN 2

char data24bytes[] = "+0000a+0000b+0000c+0000d";

void setup() {
  Serial.begin(115200);
  //Serial1.begin(115200); // Mở kết nối UART với tốc độ 115200 bps
  radio.begin();
  radio.openReadingPipe(1, 0xF0F0F0F066LL);  // Địa chỉ nhận của RF Nano
  radio.startListening();
  pinMode(LED_PIN, OUTPUT);
}

// Hàm so sánh chuỗi
bool compareStrings(const char *str1, const char *str2) {
  return strcmp(str1, str2) == 0;
}

void loop() {
  if (radio.available()) {
    char receivedData[sizeof(data24bytes)];
    radio.read(receivedData, sizeof(receivedData));

    // In dữ liệu nhận được ra Serial Monitor
    // Serial.print("Đã nhận từ RF Nano: ");
    // Serial.println(receivedData);

    // Truyền dữ liệu qua UART
      Serial.write(receivedData, sizeof(receivedData));
      Serial.flush();    // Chắc chắn dữ liệu đã được gửi trước khi tiếp tục

    // So sánh chuỗi và nhấp nháy LED nếu đúng chuỗi
    if (compareStrings(receivedData, data24bytes)) {
      digitalWrite(LED_PIN, HIGH);  // Bật LED
      delay(500);                  // Đợi 0.5 giây
      digitalWrite(LED_PIN, LOW);   // Tắt LED
      delay(500);                  // Đợi 0.5 giây

    }
  }
}
