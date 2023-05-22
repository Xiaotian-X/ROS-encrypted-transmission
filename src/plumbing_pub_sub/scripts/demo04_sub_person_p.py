import rospy
from plumbing_pub_sub.msg import person

def domsg(p):
    rospy.loginfo("%s,%d,%.2f",p.name,p.age,p.height)

if __name__ == "__main__":
    rospy.init_node("daye")

    sub = rospy.Subscriber("shetou",person,domsg,queue_size=10)
    rospy.spin()