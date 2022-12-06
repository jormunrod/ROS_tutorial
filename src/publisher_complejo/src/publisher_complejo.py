#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('twist_publisher')
pub = rospy.Publisher('/velocity', Twist, queue_size=1)
rate = rospy.Rate(2)
vel = Twist()
vel.linear.x = 0.5
vel.linear.y = 0.7
vel.linear.z = 0

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()