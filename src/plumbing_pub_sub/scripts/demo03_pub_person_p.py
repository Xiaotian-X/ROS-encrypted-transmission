import rospy
from plumbing_pub_sub.msg import person
# import rsa

if __name__ == "__main__":
    rospy.init_node("dama")

    pub = rospy.Publisher("shetou",person,queue_size=10)

    p = person()
    p.name = "李四"
    p.age = 8
    p.height = 1.85

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("%s,%d,%.2f",p.name,p.age,p.height)
        rate.sleep()
