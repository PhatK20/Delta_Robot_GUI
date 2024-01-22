#define LED_PIN 5  // Định nghĩa chân LED trên LGT RF Nano

void setup() {
  // Thiết lập chân LED là OUTPUT
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);   // Bật LED
  delay(1000);                   // Đợi 1 giây
  digitalWrite(LED_PIN, LOW);    // Tắt LED
  delay(1000);                   // Đợi 1 giây
}
