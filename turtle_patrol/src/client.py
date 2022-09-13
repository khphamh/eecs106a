#!/usr/bin/env python
import sys

import numpy as np
import rospy
from turtle_patrol.srv import Patrol  # Import service type


def patrol_client(turtle):
    turtle = str(turtle)
    # Initialize the client node
    rospy.init_node(turtle+'_patrol_client')
    # Wait until patrol service is ready
    rospy.wait_for_service('/' + turtle + '/patrol')
    try:
        # Acquire service proxy
        patrol_proxy = rospy.ServiceProxy(
            '/' + turtle + '/patrol', Patrol)
        vel = 2.0  # Linear velocity
        omega = 1.0  # Angular velocity
        x = 9
        y = 5
        theta = np.pi/2
        rospy.loginfo('Command ' + turtle + ' to patrol')
        # Call patrol service via the proxy
        patrol_proxy(vel, omega, x, y, theta)
    except rospy.ServiceException as e:
        rospy.loginfo(e)


if __name__ == '__main__':
    patrol_client(sys.argv[1])

