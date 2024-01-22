#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

void setup() {
  Serial.begin(115200);
  radio.begin();
}

void loop() {
  char text[] = "vai noi!!";
  radio.openWritingPipe(0xF0F0F0F0E1LL); // Địa chỉ pipe cho module nhận
  radio.write(&text, sizeof(text));
  delay(1000);
}
