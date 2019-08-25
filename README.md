# vidsrv

Mobile Setup:__
Download IP Webcam from Google PlayStore__
In the app enabl data logging.__
In Video Preferences change resolution to 640x480__
__
Dependencies and laptop setup:__
Install ros-kinetic-ipcamera-driver__
clone it in a catkin_workspace and run catkin_make__
__
Steps:__
1)Connect your mobile and laptop to the same network__
2)Go to the end of app and start server. You'll get the ip and port__ 
3)Go to browser and connect to the http://localhost:port set by the app(eg. http://10.60.8.174:8080)
  Check if its working.__
4)Finally, roslaunch vidsrv launch_cam_imu.launch set_url:=localhost:port__
__
You get camera and imu data in ros__


