#!/usr/bin/env python3                                                              #shebang line- Tells the operating system to use python3 and allows the file to be executed from the terminal.

import rclpy                                                                        #library for ros2
from rclpy.node import Node                                                         #import the Node class from the rclpy.node module
from std_msgs.msg import String                                                     #import the String datatype

class Talker(Node):                                                                 #talker class creation
    def __init__(self):                                                             #initialie the class
        super().__init__("talker")
        self.counter=1                                                              #counter initialization
        self.lis_pub_=self.create_publisher(String,"/chatter",10)                   #publisher creation, publishes data of String type to the topic '/chatter' and has a queue size of 10
        self.timer=self.create_timer(0.5,self.write_msg)                            #acts like an infinite while loop, calls write_msg function every 0.5 seconds
        
    def write_msg(self):                                                            #function creation
        if self.counter==1:                                                         #condition for displaying the menu
            print("1- Talker with message of your name\n",
                  "2- Talker with a welcoming message\n",
                  "3- Talker with a greeting message",sep='')
            self.menu_input=int(input("Enter the choice:- "))                       #taking input of the choice
            
        if self.menu_input==1:                                                      #when the choice entered was 1
            self.get_logger().info("Aashraey Vaid "+str(self.counter))              #prints the message on the screen
            msg=String()                                                            #creates a new String message object
            msg.data="Aashraey Vaid "+str(self.counter)                             #stores the data
            self.lis_pub_.publish(msg)                                              #publishes the data to the topic
            self.counter+=1                                                         #increment of the counter
            
        elif self.menu_input==2:                                                    #when the choice entered was 2
            self.get_logger().info("Welcome to ROS2 "+str(self.counter))            
            msg=String()
            msg.data="Welcome to ROS2 "+str(self.counter)
            self.lis_pub_.publish(msg)
            self.counter+=1
        elif self.menu_input==3:                                                   #when the choice entered was 3
            self.get_logger().info("Hello "+str(self.counter))
            msg=String()
            msg.data="Hello "+str(self.counter)
            self.lis_pub_.publish(msg)
            self.counter+=1

def main(args=None):                                                              #main function
    rclpy.init(args=args)                                                         #initializing main function
    node=Talker()                                                                 #calls the talker class
    rclpy.spin(node)                                                              #does not let the class get killed automatically and keeps the class running
    rclpy.shutdown()                                                              #kills the class on Ctrl+C

if __name__=="__main__":                                                          #ensures that script is executed directly
    main()
