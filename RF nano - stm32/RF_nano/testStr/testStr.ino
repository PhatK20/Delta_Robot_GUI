#include <SPI.h>
#include <Wire.h>
#include "RF24.h"
#include "printf.h"

RF24 SendRadio(9, 10);

char receivedData[25]; // Dùng mảng char để lưu trữ chuỗi dữ liệu

void WriteData() {
  // Đọc dữ liệu từ Serial
  if (Serial.available() >= 24) {
    Serial.readBytes(receivedData, sizeof(receivedData));

    // Mở ống gửi với địa chỉ cụ thể (0xF0F0F0F066)
    SendRadio.openWritingPipe(0xF0F0F0F066LL);

    // Gửi dữ liệu qua sóng RF
    SendRadio.write(receivedData, sizeof(receivedData));

    // In dữ liệu đã gửi ra Serial Monitor
    Serial.print("Đã gửi qua RF Nano: ");
    Serial.println(receivedData);
  }
}

void setup() {
  Serial.begin(115200);
  printf_begin();
  Serial.println(F("LGT RF-NANO v2.0 Send Test"));

  SendRadio.begin();
  SendRadio.setAddressWidth(5);
  SendRadio.setChannel(115);          //115 band above WIFI signals
  SendRadio.setPALevel(RF24_PA_MAX);  //MIN power low rage
  SendRadio.setDataRate(RF24_1MBPS);  //Minimum speed
  SendRadio.stopListening();          //Stop Receiving and start transmitting
  Serial.print("Send Setup Initialized");
  SendRadio.printDetails();
  delay(100);
}

void loop() {
  WriteData();
  delay(1000);
}
