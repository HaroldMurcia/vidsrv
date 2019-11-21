#! /usr/bin/env python
__author__="Ojit"
import requests , sys , time , urllib , json 
import rospy
from sensor_msgs.msg import Imu, LaserScan

rospy.init_node("imu_from_web",anonymous=True)

class Main(object):
    def __init__(self, url_arg="10.60.8.174:8080"):
        self.host_url="http://"+url_arg+"/sensors.json"
        print("URL set to:",self.host_url)
        self.imu_pub = rospy.Publisher("/imu0", Imu , queue_size=10)
        self.req = requests.get(self.host_url)
        self.imu_message = Imu()
        self.gyro_mean_read = [0,0,0]
        self.accel_mean_read = [0,0,0]
        self.hist_gyro = [0,0,0]
        self.hist_accel= [0,0,-9.8]
        self.rate=rospy.Rate(200)
        print("init complete")


    def get_data(self):
        self.count=0
        # [u'battery_level', u'gyro', u'proximity', u'battery_voltage', u'gravity', u'accel', u'battery_temp', u'rot_vector', u'mag', u'light', u'lin_accel']
        
        while not rospy.is_shutdown():
            # send request to server and get data in json    
            # self.req = requests.get(self.host_url,params={'gyro':'gyro','lin_accel':'lin_accel'})
            # raw_data = self.req.json()
            try:
                self.url_req = urllib.urlopen(self.host_url)
                self.raw_data = json.loads(self.url_req.read())
            except Exception as e:
                print(e)
            # self.req = grequests.get(self.host_url)
            # self.responses = grequests.map(self.req)
            # raw_data = self.responses[0].json()
            
            # get past values of raw gyro and accel data
            self.gyro_mean_read = self.raw_data['gyro']['data'][-1][1]
            self.accel_mean_read = self.raw_data['accel']['data'][-1][1]
            self.set_vals()

            #publish data
            self.imu_pub.publish(self.imu_message)
            # self.count+=1


    def set_vals(self):
        #Set data
        self.imu_message = Imu()
        self.imu_message.header.stamp = rospy.Time().now()

        self.imu_message.angular_velocity.x = self.gyro_mean_read[0]
        self.imu_message.angular_velocity.y = self.gyro_mean_read[1]
        self.imu_message.angular_velocity.z = self.gyro_mean_read[2]

        self.imu_message.linear_acceleration.x = self.accel_mean_read[0]
        self.imu_message.linear_acceleration.y = self.accel_mean_read[1]
        self.imu_message.linear_acceleration.z = self.accel_mean_read[2]




if __name__ == "__main__":
    # try:
    i = Main(sys.argv[1])
    i.get_data()
    # except Exception as e:
    #     print("provide url after hosting on web. Follow Readme")
    #     print(e)
