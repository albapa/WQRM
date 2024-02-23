#include "AccelStepper.h"
#include <Arduino.h>
#include "TCA9548A.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

#define dirPin 2
#define stepPin 3
#define motorInterfaceType 1
#define stepsPerRevolution 3200

Adafruit_MPU6050 mpu;
TCA9548A I2CMux;

const int REED_PIN = 4;

bool InCalibrate = 0;

AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);

void setup()
{  
  // Stepper Setup
  Serial.begin(9600);
  stepper.setMaxSpeed(60 * (stepsPerRevolution / 60));
  stepper.setSpeed(60 * (stepsPerRevolution / 60));
  stepper.setAcceleration(1000000);

  // Reed Setup
  pinMode(REED_PIN, INPUT_PULLUP);

  // Data Collection Setup
  I2CMux.begin(Wire);
  I2CMux.closeAll();

  // THIS CAN BE UNNOTED WHEN SOLDER JOINTS ARE FIXED
  // I2CMux.openChannel(2);
  // Serial.println("Channel 2"); // Channel 2
  // if (!mpu.begin()) {
  //   Serial.println("Failed to find MPU6050 chip (2)");
  //   while (1) {
  //     delay(10);
  //   }
  // }
  // mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  // mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  // mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  // Serial.println("");
  // delay(10);
  // I2CMux.closeChannel(2);  

  I2CMux.openChannel(3);
  Serial.println("Channel 3");
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip (3)");
    while (1) {
      delay(10);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("");
  delay(10);
  I2CMux.closeChannel(3);

}

void loop(){  

  if (Serial.available() > 0) {
    String Key = Serial.readStringUntil('\n');
    
    if (Key.charAt(0) == 'S') {
        String SpeedString = Key.substring(2, 4);
        int Speed = SpeedString.toInt();
        stepper.setMaxSpeed(Speed * (stepsPerRevolution / 60));
        stepper.moveTo(stepper.currentPosition() + (10 * stepsPerRevolution));
    }
    else if (Key.charAt(0) == 'O') {
        String SpeedString = Key.substring(2, 4);
        int Speed = SpeedString.toInt();
        stepper.setMaxSpeed(Speed * (stepsPerRevolution / 60));
        stepper.moveTo(stepper.currentPosition() + (Key.substring(4, 5).toInt() * stepsPerRevolution));        
    }
    else if (Key.charAt(0) == 'Q') {
        stepper.moveTo(stepper.currentPosition());
    }
    else if (Key.charAt(0) == 'D') {
      sensors_event_t a, g, temp;
      // THIS CAN BE UNNOTED WHEN SOLDER JOINTS ARE FIXED
      // I2CMux.openChannel(2);
      // mpu.getEvent(&a, &g, &temp);
      // Serial.print("2AcX:" + String(a.acceleration.x) + ",2AcY:" + String(a.acceleration.y) + ",2AcZ:" + String(a.acceleration.z) + "\n");
      // I2CMux.closeChannel(2);

      I2CMux.openChannel(3);
      mpu.getEvent(&a, &g, &temp);
      Serial.print("3AcX:" + String(a.acceleration.x) + ",3AcY:" + String(a.acceleration.y) + ",3AcZ:" + String(a.acceleration.z) + "\n");
      I2CMux.closeChannel(3);

    }
    else if (Key.charAt(0) == 'P') {
      InCalibrate = 1;
      Serial.println("CalibrateMode");
      stepper.setMaxSpeed(20 * (stepsPerRevolution / 60));
    }
}

if (InCalibrate == 1) {
  int proximity = digitalRead(REED_PIN);
  if (proximity == 1) {
    stepper.moveTo(stepper.currentPosition() + 16);
  } else if (proximity == 0) {
    stepper.moveTo(stepper.currentPosition() + 0);
    stepper.moveTo(stepper.currentPosition() + 32);
    Serial.println("Calibrated");
    InCalibrate = 0;
  }
}

stepper.run();
// Serial.println(stepper.currentPosition());
}
