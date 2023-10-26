#!/usr/bin/env python3

#--------Include modules---------------
from ast import Is
from copy import copy
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PointStamped, PoseStamped 
import tf
from numpy import array,vstack,delete
from sklearn.cluster import MeanShift
from rrt_exploration.msg import PointArray
from shapely.geometry import Point as pt
from shapely.geometry.polygon import Polygon
from shapely.geometry import  LineString
from zoe_interface.msg import fiducial
from rrt_exploration.srv import Floor, FloorRequest
import time

# Subscribers' callbacks------------------------------


# Node----------------------------------------------
def node():
	rospy.init_node('filter', anonymous=False)
	
	pub= rospy.Publisher('goaltospot', PoseStamped, queue_size=10)
	goal= PoseStamped()
	time.sleep(2)
	print("dovrebbe fare cose ora")
	goal.pose.position.x=-2
	goal.pose.position.y=-2
	pub.publish(goal)
	print("pubblicato 1")
	time.sleep(10)
	goal.pose.position.x=0.0
	goal.pose.position.y=3.0
	pub.publish(goal)
	print("pubblicato 2")
	time.sleep(10)
	goal.pose.position.x=2.0
	goal.pose.position.y=-2.0
	pub.publish(goal)
	print("pubblicato 3")
	goal.pose.position.x=-3.0
	goal.pose.position.y=1.0
	pub.publish(goal)
	print("pubblicato 4")
	goal.pose.position.x=3.0
	goal.pose.position.y=1.0
	pub.publish(goal)
	print("pubblicato 5")
	goal.pose.position.x=-2.0
	goal.pose.position.y=-2.0
	pub.publish(goal)
	print("pubblicato 1")
	
if __name__ == '__main__':
	try:
		node()
	except rospy.ROSInterruptException:
		pass
 
 
 
 
