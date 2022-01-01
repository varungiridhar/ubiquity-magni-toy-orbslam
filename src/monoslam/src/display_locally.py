#!/usr/bin/env python3
import rospy

import json
import sys
from pointmap import Map
from display import Display3D
import pangolin
from threading import Thread
from std_msgs.msg import String

class map_display:
    def __init__(self):
        self.subscriber = rospy.Subscriber("/data/3Dmap/json", String, self.callback, queue_size = 10)
        self.disp3d = Display3D()
    def callback(self, ros_data):
        print("callback called")
        data = ros_data.data
        mapp = Map()
        mapp.deserialize(data)
        print(mapp)
        print("paint")
        self.disp3d.paint(mapp)

def main(args):
    md = map_display()
    #filename = sys.argv[1]
    #f = open(filename)
    rospy.init_node('monoslam', anonymous=True)
    rospy.spin()
    #data = json.load(f)
    #mapp = Map()
    #mapp.deserialize(data)
    #print(mapp)
    #disp3d = Display3D()
    #i = 0
    #try:
    #    while True:
    #        if disp3d is not None and i % 10000 == 0:
    #            print("paint")
    #            disp3d.paint(mapp)
    #            i += 1
    #except KeyboardInterrupt:
    #    pass

if __name__ == '__main__':
    main(sys.argv)
