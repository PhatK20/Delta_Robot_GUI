#include <SPI.h>
#include <RF24.h>
#include <string.h>
#include <AccelStepper.h>

#define limitSwitch1 22 // thta 2
#define limitSwitch2 24 // thta 3
#define limitSwitch3 26 // thta 1

// Khởi tạo đối tượng stepper với chân driver (STEP, DIR) // theta 3 duong di len
                                                          // theta 2 duong di len
                                                          
AccelStepper stepper1(AccelStepper::DRIVER, 2, 3);
AccelStepper stepper2(AccelStepper::DRIVER, 4, 5);
AccelStepper stepper3(AccelStepper::DRIVER, 6, 7);

RF24 radio(9, 10); // CE, CSN

static volatile int node1, node2, node3, node4;
static volatile float tmp_node1, tmp_node2, tmp_node3, tmp_node4;

const int totalSteps = 66327 ; // Tổng số bước trong một vòng
static volatile int flag_home = 0;

int degreesToSteps(float degrees) 
{
  float steps = degrees / 360.0 * totalSteps;
  return int(steps);
}

void Homing(void)
{
  while (digitalRead(limitSwitch2) == HIGH) 
  {
    stepper2.setSpeed(-5000);
    stepper2.runSpeed();
  }
  stepper2.setCurrentPosition(0);
  // Chờ một khoảng thời gian ngắn
  delay(1000);

  // while (digitalRead(limitSwitch3) == HIGH)
  // {
  //   stepper3.setSpeed(5000);
  //   stepper3.runSpeed();
  // }
  // stepper3.setCurrentPosition(0);
  // // Chờ một khoảng thời gian ngắn
  // delay(1000);

  while (digitalRead(limitSwitch1) == HIGH)
  {
    stepper1.setSpeed(-5000);
    stepper1.runSpeed();
  }
  stepper1.setCurrentPosition(0);
  // Chờ một khoảng thời gian ngắn
  delay(1000);
  stepper1.moveTo(0);
  stepper2.moveTo(0);
  stepper3.moveTo(0);

}

void setup() 
{
  Serial.begin(115200);
  radio.begin();
  radio.openReadingPipe(1, 0xF0F0F0F0E1LL); // Địa chỉ pipe cho module gửi
  radio.startListening();
  pinMode(limitSwitch1, 2);
   pinMode(limitSwitch2, 2);
    pinMode(limitSwitch3, 2);

  // Thiết lập tốc độ tối đa và gia tốc cho stepper
  stepper1.setMaxSpeed(20000);
  stepper1.setAcceleration(20000);

  stepper2.setMaxSpeed(20000);
  stepper2.setAcceleration(20000);

  stepper3.setMaxSpeed(20000);
  stepper3.setAcceleration(20000);

  stepper1.moveTo(0);
  stepper2.moveTo(0);
  stepper3.moveTo(0);
  // Homing();
    // stepper1.moveTo(-4000);
    // stepper2.moveTo(-4000);
    stepper3.moveTo(-4000);

}

void loop()
{
  if (radio.available()) 
  {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);
    if((sscanf(text, "%da%db%dc%dd", &node1, &node2, &node3, &node4)) == 4)
	  {
      // Serial.println(node1);
      // Serial.println(node2);   
      // Serial.println(node3);   
      // Serial.println(node4);
      
      tmp_node1 = node1;
      tmp_node2 = node2;
      tmp_node3 = node3;

      tmp_node1 = degreesToSteps(tmp_node1);
      tmp_node2 = degreesToSteps(tmp_node2);
      tmp_node3 = degreesToSteps(tmp_node3);

      node1 = tmp_node1;
      node2 = tmp_node2 *100;
      Serial.println(node1);
      Serial.println(node2);   

      // stepper1.moveTo((int)tmp_node1);
      stepper2.moveTo(node2);
      // stepper3.moveTo((int)tmp_node3);
    }
  }
  // if(digitalRead(26) != 1)
  // {
  //   Serial.println("Heloo");
  // }
      
  stepper1.run();
  stepper2.run();
  stepper3.run();


}
