#!/bin/bash

echo "Setting up environment"
source devel/setup.bash

export ROS_MASTER_URI=http://10.10.200.1:11311
export ROS_IP=10.10.200.3

echo "Finished sourcing and setting environment variables"

