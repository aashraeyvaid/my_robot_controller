#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from functools import partial

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.chat_subscriber_=self.create_subscription(String,"/chatter",self.chatter_callback,10)
        self.get_logger().info("Listener has been started")
    
    def chatter_callback(self,msg:String):
        self.get_logger().info("Listened "+msg.data)

def main(args=None):
    rclpy.init(args=args)
    node=Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()