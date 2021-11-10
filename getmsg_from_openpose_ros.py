#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys
from sensor_msgs.msg import Image,CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from openpose_ros_msgs.msg import OpenPoseHumanList,OpenPoseHuman
import cv2
from std_msgs.msg import String

#==========================================

def callback(data):
    print("CallBack")
    for box in data.human_list:
        print(box.body_key_points_with_prob[4].x)
        print(box.body_key_points_with_prob[4].y)
        #print(box.body_key_points_with_prob[7].x)
        #print(box.body_key_points_with_prob[7].y)
        """
        print(box.body_key_points_with_prob[3])
        xavr = (box.body_key_points_with_prob[3].x + box.body_key_points_with_prob[4].x)*0.5
        yavr = (box.body_key_points_with_prob[3].y + box.body_key_points_with_prob[4].y)*0.5
        print(xavr)
        print(yavr)
        """

def main():
    rospy.init_node('cat_openpose')
    rospy.sleep(1) 
    rospy.Subscriber('/openpose_ros/human_list', OpenPoseHumanList, callback)
    rospy.spin()


if __name__ == '__main__':
    try :
        print("start")  
        main()
    except rospy.ROSInterruptException:
        sys.exit()

    try:
        rospy.sleep(1)
        print("fin") 
    except:
        rospy.logerr('fail')
        sys.exit()