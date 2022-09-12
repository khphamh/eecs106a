#!/usr/bin/env python

import sys
from geometry_msgs.msg import Vector3

from geometry_msgs.msg import Twist
import rospy
def move_turtle(turtle):
    turtle = str(turtle)

    pub = rospy.Publisher(turtle+"/cmd_vel", Twist, queue_size=10)
    r = rospy.Rate(10)
    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        x = input()        
        if x == "w":
            pub.publish( Vector3(1,0,0) , Vector3(0,0,0) )
        elif x == "a":
            pub.publish(Vector3(0,0,0) , Vector3(0,0,1) )
        elif x == "s":
            pub.publish(Vector3(-1,0,0) , Vector3(0,0,0))
        elif x == "d":
            pub.publish( Vector3(0,0,0) , Vector3(0,0,-1))

        #print(rospy.get_name() + ": I sent \"%s\"" % pub_string)
        
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':
    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('move_turtle', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
    	move_turtle(sys.argv[1])
    except rospy.ROSInterruptException: pass
