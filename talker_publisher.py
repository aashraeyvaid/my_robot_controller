#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.counter=1
        self.lis_pub_=self.create_publisher(String,"/chatter",10)
        self.timer=self.create_timer(0.5,self.write_msg)
    def write_msg(self):
        if self.counter==1:
            print("1- Talker with message of your name\n",
                  "2- Talker with a welcoming message\n",
                  "3- Talker with a greeting message",sep='')
            self.menu_input=int(input("Enter the choice:- "))
        if self.menu_input==1:
            self.get_logger().info("Aashraey Vaid "+str(self.counter))
            msg=String()
            msg.data="Aashraey Vaid "+str(self.counter)
            self.lis_pub_.publish(msg)
            self.counter+=1
        elif self.menu_input==2:
            self.get_logger().info("Welcome to ROS2 "+str(self.counter))
            msg=String()
            msg.data="Welcome to ROS2 "+str(self.counter)
            self.lis_pub_.publish(msg)
            self.counter+=1
        elif self.menu_input==3:
            self.get_logger().info("Hello "+str(self.counter))
            msg=String()
            msg.data="Hello "+str(self.counter)
            self.lis_pub_.publish(msg)
            self.counter+=1

def main(args=None):
    rclpy.init(args=args)
    node=Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
