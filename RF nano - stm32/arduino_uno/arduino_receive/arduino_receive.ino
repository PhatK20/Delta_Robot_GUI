#include <RF24.h>

RF24 radio(9, 10);  // Chân CE, CSN

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openReadingPipe(1, 0xF0F0F0F066LL);  // Địa chỉ nhận của RF Nano
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    char receivedData[25];
    radio.read(receivedData, sizeof(receivedData));

    // Truyền dữ liệu qua UART
    Serial.write(receivedData, sizeof(receivedData));
    Serial.flush();    // Chắc chắn dữ liệu đã được gửi trước khi tiếp tục
  }
}
