#!/usr/bin/env/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.duration import Duration
from turtlesim.msg import Pose
import math

class DrawEllipse(Node):
    def __init__(self):
        super().__init__("draw_ellipse")
        self.a=2.0
        self.b=1.0
        self.theta=0.0
        self.omega=1.0
        self.amc_vel_pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_sub_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.timer=self.create_timer(0.5,self.draw_ellipse)
        self.get_logger().info("draw_ellipse node has started...")
    
    def pose_callback(self,msg:Pose):
        self.theta=msg.theta

    def draw_ellipse(self):
        msg=Twist()
        t = self.get_clock().now().nanoseconds / 1e9
        theta_param = self.omega * t
        dx = -self.a * self.omega * math.sin(theta_param)
        dy = self.b * self.omega * math.cos(theta_param)
        v = math.sqrt(dx**2 + dy**2)
        heading = math.atan2(dy, dx)
        angle_diff = self.normalize_angle(heading - self.theta)
        msg.linear.x = v
        msg.angular.z = angle_diff * 2.0
        self.amc_vel_pub_.publish(msg)

    
    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle


def main(args=None):
    rclpy.init(args=args)
    node=DrawEllipse()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()