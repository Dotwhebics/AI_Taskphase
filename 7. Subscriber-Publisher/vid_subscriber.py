#! /usr/bin/python3

import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def get_frame(message):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(message)
    cv.imshow("Video Feed", frame)
    cv.waitKey(1)

def subscribe():
    rospy.init_node('Video_Receiver', anonymous = True)
    rospy.Subscriber('Video_Pipeline', Image, get_frame)
    rospy.spin()

if __name__ == '__main__':
    subscribe()
