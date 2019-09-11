#include <MPU9250_asukiaaa.h>
#include <WiFi.h>
#include <ros.h>
#include <sensor_msgs/Imu.h>

#define SDA_PIN 21
#define SCL_PIN 22

MPU9250_asukiaaa mySensor;

const char *ssid = "rover-esp";
const char *password = "123456789";
//for rosserial server
IPAddress server(192,168,4,2);            // Laptop's IP address
const uint16_t serverPort = 11411;

ros::NodeHandle nh;
sensor_msgs::Imu imu_data;
ros::Publisher imu_pub("Imu", &imu_data);


void setup() {
  Serial.begin(115200);

  // for esp32
  Wire.begin(SDA_PIN, SCL_PIN); //sda, scl

  mySensor.setWire(&Wire);
  mySensor.beginAccel();
  mySensor.beginMag();
  mySensor.beginGyro();
  
  WiFi.softAP(ssid,password);
  IPAddress myIP = WiFi.softAPIP();

  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();

  nh.advertise(imu_pub);

  delay(100);
  Serial.println("setup complete");
}

void loop() {
  // put your main code here, to run repeatedly:
if(nh.connected()){
    mySensor.accelUpdate();
    mySensor.magUpdate();
    mySensor.gyroUpdate();
  
    //Set imu accel values
    imu_data.linear_acceleration.x = mySensor.accelX();
    imu_data.linear_acceleration.y = mySensor.accelY();
    imu_data.linear_acceleration.z = mySensor.accelZ();

    //Set imu gyro values
    imu_data.angular_velocity.x = mySensor.gyroX();
    imu_data.angular_velocity.y = mySensor.gyroY();
    imu_data.angular_velocity.z = mySensor.gyroZ();
  
    // publish the data
    imu_pub.publish(&imu_data);
  }
  else{
    Serial.println("NOT CONNECTED!!");  
  }
  nh.spinOnce();
  delay(5);
}
