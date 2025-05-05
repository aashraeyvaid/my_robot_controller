#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyListener(Node):
    def __init__(self):
        super().__init__("my_listener")
        self.counter=1
        self.lis_pub_=self.create_publisher(String,"/chatter",10)
        self.timer=self.create_timer(0.5,self.write_msg)
    def write_msg(self):
        self.get_logger().info("Hello Aashraey Vaid "+str(self.counter))
        msg=String()
        msg.data="Hello Aashraey Vaid "+str(self.counter)
        self.lis_pub_.publish(msg)
        self.counter+=1

def main(args=None):
    rclpy.init(args=args)
    node=MyListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()