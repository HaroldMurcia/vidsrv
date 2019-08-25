# vidsrv

Mobile Setup:

1)Download IP Webcam from Google PlayStore

2)In the app enabl data logging.

3)In Video Preferences change resolution to 640x480.



Dependencies and laptop setup:

1)Install ros-kinetic-ipcamera-driver.

2)clone it in a catkin_workspace and run catkin_make.


Steps:

1)Connect your mobile and laptop to the same network

2)Go to the end of app and start server. You'll get the ip and port

3)Go to browser and connect to the http://localhost:port set by the app(eg. http://10.60.8.174:8080)
  Check if its working.
  
4)Finally, roslaunch vidsrv launch_cam_imu.launch set_url:=localhost:port


You get camera and imu data in ros



