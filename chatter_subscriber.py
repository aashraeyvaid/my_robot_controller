#!/usr/bin/env python3                                                                                    #shebang line

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from functools import partial

class Listener(Node):                                                                                     #creation of listener class
    def __init__(self):
        super().__init__("listener")
        self.chat_subscriber_=self.create_subscription(String,"/chatter",self.chatter_callback,10)        #subscriber creation, subscribes the data of String type from the '/chatter' topic and calls chatter_callback function, has a queue size of 10
        self.get_logger().info("Listener has been started")                                               #prints the message on the screen
    
    def chatter_callback(self,msg:String):                                                                #function creation
        self.get_logger().info("Listened "+msg.data)                                                      #prints the subscribed data on the screen

def main(args=None):                                                                                      #main function
    rclpy.init(args=args)
    node=Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
