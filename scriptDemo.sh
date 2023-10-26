#!/bin/bash
gnome-terminal --tab --title="spot" -- bash -c "roslaunch zoe_interface spot.launch"
sleep 5
gnome-terminal --tab --title="vel" -- bash -c "roslaunch zoe_interface vel.launch"
sleep 1
gnome-terminal --tab --title="expl" -- bash -c "roslaunch zoe_exploration single.launch"
sleep 2
sleep 5
gnome-terminal --tab --title="floor2" -- bash -c "roslaunch zoe_map floor2.launch"
sleep 5
gnome-terminal --tab --title="service" -- bash -c "rosservice call /floor2/pause; rosservice call /floor2/reset"
sleep 5
gnome-terminal --tab --title="floor" -- bash -c "roslaunch zoe_map map.launch"
sleep 5 
gnome-terminal --tab --title="floor" -- bash -c "roslaunch zoe_new movelaunch.launch"
#gnome-terminal --tab --title="nav" -- bash -c "roslaunch zoe_navigation teb.launch"

#gnome-terminal --tab --title="clic" -- bash -c "rosrun zoe_exploration clicked_points.py"
#gnome-terminal --tab --title="stairs" -- bash -c "rosrun zoe_navigation stairdetection.py"
