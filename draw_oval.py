#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.duration import Duration


class DrawOvalNode(Node):

    def __init__(self):
        super().__init__("draw_oval")
        self.timer_period=0.5
        self.timer=self.create_timer(self.timer_period,self.timer_callback)

        self.state="big"
        self.state_start_time=self.get_clock().now()

        self.duration_big=Duration(seconds=2.183782484)
        self.duration_small=Duration(seconds=0.8230336921)

        self.cycle_count=0
        self.max_count=9

        self.amc_vel_pub_ =self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("Draw oval node has been started")

    def timer_callback(self):
        now=self.get_clock().now()
        elapsed=now -self.state_start_time
        if self.state=="big":
            self.big_circle()
            if elapsed>self.duration_big:
                self.state="small"
                self.state_start_time=now

        elif self.state=="small":
            self.small_circle()
            if elapsed>self.duration_small:
                self.state="big"
                self.cycle_count+=1
                self.state_start_time=now
            
            if self.cycle_count>=self.max_count:
                rclpy.shutdown()

    def big_circle(self):
        msg=Twist()
        msg.linear.x=4.0
        msg.angular.z=1.0
        self.amc_vel_pub_.publish(msg)

    def small_circle(self):
        msg=Twist()
        msg.linear.x=1.5
        msg.angular.z=1.0
        self.amc_vel_pub_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node=DrawOvalNode()
    rclpy.spin(node)


if __name__=="__main__":
    main()
