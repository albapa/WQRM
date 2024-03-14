#include <Arduino.h>
#include "TCA9548A.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
TCA9548A I2CMux;   

void setup() {
  Serial.begin(57600); // Set the baud rate to match the receiver
  Serial1.begin(9600); // Set the baud rate to match the receiver

    I2CMux.begin(Wire);             // Wire instance is passed to the library

  I2CMux.closeAll();              // Set a base state which we know (also the default state on power on)
  
  I2CMux.openChannel(2);
  //Serial.println("Channel 2"); // Channel 2
    // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  //Serial.println("");
  delay(10);
  I2CMux.closeChannel(2);

  I2CMux.openChannel(3);
  //Serial.println("Channel 3");
    // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  //Serial.println("");
  delay(10);
  I2CMux.closeChannel(3);
}

void loop() {
  if (Serial.available() > 0) {
    String dataToSend = Serial.readStringUntil('\n'); // Read the string from Serial Monitor until a newline character
    Serial1.println(dataToSend); // Assuming you're using a hardware serial (e.g., Serial1) for communication with the receiver

  }

  sensors_event_t a, g, temp;
  I2CMux.openChannel(2);
  mpu.getEvent(&a, &g, &temp);
  Serial.print(String(a.acceleration.x) + (",") + String(a.acceleration.y) + (",") + String(a.acceleration.z) + (","));
  I2CMux.closeChannel(2);
  I2CMux.openChannel(3);
  mpu.getEvent(&a, &g, &temp);
  Serial.print(String(a.acceleration.x) + (",") + String(a.acceleration.y) + (",") + String(a.acceleration.z) + "\n");
  I2CMux.closeChannel(3);
}