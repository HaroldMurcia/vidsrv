# vidsrv 8-)  
## This package allows you to stream your android mobile camera and sensor data to ROS by scraping it from a web server. 
***
### Mobile Setup:  
* Download IP Webcam from Google PlayStore, an app that lets you stream your mobile sensor data to web server.  
* In the application enable data logging.  
* In Video Preferences change resolution to 640x480.  
***


### Dependencies and laptop setup:
* Install ros-kinetic-ipcamera-driver.  
```
 $ mkdir -p catkin_ws_vid/src && cd catkin_ws_vid/src
 $ git clone https://github.com/ojitmehta123/vidsrv.git
 $ cd .. && catkin_make
 $ source devel/setup.bash
```
---

### Steps To Run:

* Connect your mobile and laptop to the same network

* Go to the end of app and start server. You'll get the ip and port

* Go to browser and connect to the http://localhost:port set by the app(eg. http://10.60.8.174:8080)
  Check if its working. 
  
* Finally,  
 ```
 $ roslaunch vidsrv launch_cam_imu.launch set_url:=localhost:port
```

## You get camera and imu data in ros



