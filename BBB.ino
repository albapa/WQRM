#include "AccelStepper.h"
//#include <Arduino.h>
//#include "TCA9548A.h"
//#include <Adafruit_MPU6050.h>
//#include <Adafruit_Sensor.h>
//#include <Wire.h>

#define dirPin 2
#define stepPin 3
#define motorInterfaceType 1
#define stepsPerRevolution 3200

//Adafruit_MPU6050 mpu;
//TCA9548A I2CMux;

const int REED_PIN = 4;

bool InCalibrate = 0;

AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);

void setup(){
  // Stepper Setup
  Serial1.begin(9600);
  stepper.setMaxSpeed(((60 * (stepsPerRevolution / 60)))*1.5);
  stepper.setSpeed(60 * (stepsPerRevolution / 60));
  stepper.setAcceleration(100000000);

  // Reed Setup
  pinMode(REED_PIN, INPUT_PULLUP);

}

void loop(){  

  if (Serial1.available() > 0) {
    String Key = Serial1.readStringUntil('\n');
    
    if (Key.charAt(0) == 'S') {
        String SpeedString = Key.substring(2, 4);
        int Speed = SpeedString.toInt();
        stepper.setMaxSpeed((Speed * (stepsPerRevolution / 60))*1.1);
        stepper.moveTo(stepper.currentPosition() + (10 * stepsPerRevolution));
    }
    else if (Key.charAt(0) == 'O') {
        String SpeedString = Key.substring(2, 4);
        int Speed = SpeedString.toInt();
        stepper.setMaxSpeed((Speed * (stepsPerRevolution / 60))*1.1);
        stepper.moveTo(stepper.currentPosition() + (Key.substring(4, 5).toInt() * stepsPerRevolution));        
    }
    else if (Key.charAt(0) == 'Q') {
        stepper.moveTo(stepper.currentPosition());
    }
    else if (Key.charAt(0) == 'D') {
      // Data

    }
    else if (Key.charAt(0) == 'P') {
      InCalibrate = 1;
      Serial1.println("CalibrateMode");
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
    Serial1.println("Calibrated");
    InCalibrate = 0;
  }
}

stepper.run();

}