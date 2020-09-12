#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897


def move():
    # Starts a new node
    rospy.init_node('turlesim_project', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move our robot")
    #setting the linear angular speed for movement
    speed = 1
    angular_speed = 30*2*PI/360

    #Checking if the movement is forward or backwards

    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    while not rospy.is_shutdown():
            ui = raw_input()
            isForward = ui
            if(isForward == 'w'):
                vel_msg.angular.z = 0
                vel_msg.linear.x = abs(speed)
            elif(isForward == 's'):
                vel_msg.angular.z = 0
                vel_msg.linear.x = -abs(speed)
            elif(isForward == 'a'):
                vel_msg.linear.x = 0
                vel_msg.angular.z = abs(angular_speed)
            elif(isForward == 'd'):
                vel_msg.linear.x = 0
                vel_msg.angular.z = -abs(angular_speed)
            #Publish the velocit
            velocity_publisher.publish(vel_msg)
            isForward = None

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
