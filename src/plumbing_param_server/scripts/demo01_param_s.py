#!/usr/bin/env python2
import rospy
from std_msgs.msg import Int32
import socket
 
rospy.init_node('topic_publisher')
pub = rospy.Publisher('counter',Int32, queue_size=10)
rate = rospy.Rate(2)
 
server = socket.socket()
server.bind(('localhost', 1666))
server.listen(5)
 
exit = ''
while True:
    con, addr = server.accept()
    print('connect_addr: ', addr)
    while con:
        msg = con.recv(1024).decode('utf-8')
        if msg[0:2] == 'ab' and msg[-2:] == 'cd':
            while not rospy.is_shutdown():
 
                pub.publish(int(msg[2:6]))
                rate.sleep()
 
            if msg == 'break':
                con.close()
                exit = 'break'
                break
    if exit == 'break':
        break
server.close()