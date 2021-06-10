#! /usr/bin/python3

import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def send_frame():
    capture = cv.VideoCapture(0)
    send = rospy.Publisher('Video_Pipeline', Image, queue_size = 10)
    rospy.init_node('Video_Sender', anonymous = True)
    rate = rospy.Rate(20)
    bridge = CvBridge()
    while not rospy.is_shutdown():
        istrue, frame = capture.read()
        rospy.loginfo('Publishing single frame')
        message = bridge.cv2_to_imgmsg(frame)
        send.publish(message)
    rate.sleep()

if __name__ == '__main__':
    try:
        send_frame()
    except rospy.ROSInterruptException:
        exit()

